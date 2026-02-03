import os
from aiogram import Router, F, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
import pandas as pd
from io import BytesIO

from app.services.parser import parse_excel
from app.services.validator import validate_smeta
from app.services.scoring import score_smeta
from app.services.recommendations import get_recommendations, enhance_recommendations
# Optionally import feature enrichment if needed
from app.services.features import add_features

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Hello! I am the AI Budget Inspector.\n\n"
        "Send me an Excel file (.xlsx) with your estimate (smeta), "
        "and I will analyze it for errors, anomalies, and provide recommendations."
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📋 **Instructions**:\n"
        "1. Prepare your budget in Excel format.\n"
        "2. Send the file here.\n"
        "3. Wait for the analysis report.\n\n"
        "The file should have columns roughly matching: category, name, quantity, unit_price..."
    )

@router.message(F.document)
async def handle_document(message: Message, bot: Bot):
    doc = message.document
    if not doc.file_name.endswith(('.xlsx', '.xls')):
        await message.answer("⚠️ Please send a valid Excel file (.xlsx or .xls).")
        return

    await message.answer("⏳ Analyzing your file... Please wait.")

    # Download file
    file_io = BytesIO()
    await bot.download(doc, destination=file_io)
    file_io.seek(0)

    try:
        # 1. Parse using existing service
        df = parse_excel(file_io)
        
        # 2. Add features
        df = add_features(df)

        # 3. Validate
        validation_results = validate_smeta(df)

        # 4. Score
        score = score_smeta(validation_results, df)

        # 5. Recommendations
        recs = get_recommendations(validation_results, df)
        recs = enhance_recommendations(df, recs)

        # Format Response
        response_text = f"📊 **Analysis Result**\n\n"
        response_text += f"**Quality Score**: {score}/100\n"
        
        if score >= 90:
            response_text += "✅ Excellent! Minor adjustments only.\n"
        elif score >= 70:
            response_text += "⚠️ Good, but check the warnings.\n"
        else:
            response_text += "❌ Creating significant risks. Review immediately.\n"
        
        response_text += "\n**Top Recommendations**:\n"
        # Limit to top 5 recommendations to avoid spamming
        for i, rec in enumerate(recs[:5], 1):
            response_text += f"{i}. {rec}\n"
        
        if len(recs) > 5:
            response_text += f"\n...and {len(recs)-5} more issues found."

        await message.answer(response_text)

        # Future: Send charts here once visualizer is ready

    except Exception as e:
        await message.answer(f"❌ An error occurred during analysis: {str(e)}")
