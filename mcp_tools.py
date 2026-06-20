"""
mcp_tools.py

This module defines mock data structures and tooling functions for Mandi Prices,
Government Subsidies/Schemes, and Weather-Based Irrigation advice. It simulates
a structured Model Context Protocol (MCP) server environment.
"""

from typing import Dict, Any, List

# 1. Mock Datasets for Rajasthan Agricultural Context

MANDI_PRICES: Dict[str, Dict[str, Any]] = {
    "mustard": {
        "crop_name_en": "Mustard (Sarson)",
        "crop_name_hi": "सरसों (Mustard)",
        "rate": "₹5,600 per quintal",
        "trend_en": "Upwards (+4.5% over last 30 days due to strong oil-mill demand and lower winter yield).",
        "trend_hi": "ऊपर की ओर (+4.5% पिछले 30 दिनों में, तेल मिलों की मजबूत मांग और कम शीतकालीन पैदावार के कारण)।",
        "arrival_status_en": "High arrivals in Bharatpur and Alwar markets.",
        "arrival_status_hi": "भरतपुर और अलवर मंडियों में अधिक आवक।"
    },
    "wheat": {
        "crop_name_en": "Wheat (Gehun)",
        "crop_name_hi": "गेहूं (Wheat)",
        "rate": "₹2,450 per quintal",
        "trend_en": "Stable (Fluctuations within ±1% as post-harvest arrivals match government MSP procurement).",
        "trend_hi": "स्थिर (सरकारी न्यूनतम समर्थन मूल्य खरीद के साथ कटाई के बाद की आवक मेल खाने से ±1% के भीतर उतार-चढ़ाव)।",
        "arrival_status_en": "Steady arrivals across Kota and Sri Ganganagar.",
        "arrival_status_hi": "कोटा और श्रीगंगानगर में स्थिर आवक।"
    },
    "guar": {
        "crop_name_en": "Guar Seed",
        "crop_name_hi": "ग्वार (Guar)",
        "rate": "₹4,800 per quintal",
        "trend_en": "Downwards (-3.2% due to sluggish export demand from hydraulic fracturing industries).",
        "trend_hi": "नीचे की ओर (-3.2% हाइड्रोलिक फ्रैक्चरिंग उद्योगों से मंद निर्यात मांग के कारण)।",
        "arrival_status_en": "Moderate arrivals in Western Rajasthan markets.",
        "arrival_status_hi": "पश्चिमी राजस्थान की मंडियों में सामान्य आवक।"
    }
}

SCHEMES: List[Dict[str, Any]] = [
    {
        "id": "pm_kisan",
        "name_en": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        "name_hi": "पीएम-किसान (प्रधानमंत्री किसान सम्मान निधि योजना)",
        "max_land_hectares": 2.0,
        "benefit_en": "₹6,000 yearly direct income support in three equal installments of ₹2,000.",
        "benefit_hi": "प्रति वर्ष ₹6,000 की सीधी आय सहायता, ₹2,000 की तीन समान किस्तों में।"
    },
    {
        "id": "solar_pump",
        "name_en": "Rajasthan Solar Pump Subsidy (PM-KUSUM Component B)",
        "name_hi": "राजस्थान सौर ऊर्जा पंप अनुदान योजना (पीएम-कुसुम)",
        "max_land_hectares": 5.0,
        "benefit_en": "Up to 60% subsidy for installing 3HP to 7.5HP solar water pumps for irrigation.",
        "benefit_hi": "सिंचाई के लिए 3HP से 7.5HP सौर ऊर्जा वाटर पंप स्थापित करने के लिए 60% तक का अनुदान।"
    },
    {
        "id": "beej_swavalamban",
        "name_en": "Mukhyamantri Beej Swavalamban Yojana",
        "name_hi": "मुख्यमंत्री बीज स्वावलम्बन योजना",
        "max_land_hectares": 2.0,
        "benefit_en": "Free or highly subsidized high-yielding variety (HYV) seeds of Wheat and Mustard for small/marginal farmers.",
        "benefit_hi": "लघु और सीमांत किसानों के लिए गेहूं और सरसों के मुफ्त या अत्यधिक अनुदानित उन्नत किस्म के बीज।"
    },
    {
        "id": "fasal_bima",
        "name_en": "PM Fasal Bima Yojana (Crop Insurance)",
        "name_hi": "प्रधानमंत्री फसल बीमा योजना (फसल बीमा)",
        "max_land_hectares": 10.0,
        "benefit_en": "Low-premium crop insurance covering yield loss due to natural calamities, pests, or diseases.",
        "benefit_hi": "प्राकृतिक आपदाओं, कीटों या बीमारियों के कारण फसल नुकसान को कवर करने वाला कम प्रीमियम का फसल बीमा।"
    }
]

WEATHER_FORECAST: Dict[str, Any] = {
    "location": "Bharatpur, Rajasthan",
    "forecast": [
        {
            "day": "Day 1 (Today)",
            "temp": "38°C",
            "condition_en": "Sunny & Dry",
            "condition_hi": "धूप और शुष्क",
            "irrigation_advice_en": "High evaporation. Water crops in early morning or late evening to minimize moisture loss.",
            "irrigation_advice_hi": "उच्च वाष्पीकरण। नमी के नुकसान को कम करने के लिए सुबह जल्दी या देर शाम को सिंचाई करें।"
        },
        {
            "day": "Day 2",
            "temp": "39°C",
            "condition_en": "Sunny & Wind",
            "condition_hi": "धूप और तेज हवाएं",
            "irrigation_advice_en": "Dry winds can stress plants. Check soil moisture and perform light watering if dry.",
            "irrigation_advice_hi": "शुष्क हवाएं पौधों को तनाव दे सकती हैं। मिट्टी की नमी की जांच करें और हल्की सिंचाई करें।"
        },
        {
            "day": "Day 3",
            "temp": "37°C",
            "condition_en": "Partly Cloudy",
            "condition_hi": "आंशिक रूप से बादल",
            "irrigation_advice_en": "Normal irrigation schedule can be maintained. No immediate rain threat.",
            "irrigation_advice_hi": "सामान्य सिंचाई कार्यक्रम जारी रखा जा सकता है। वर्षा की तत्काल संभावना नहीं है।"
        },
        {
            "day": "Day 4",
            "temp": "33°C",
            "condition_en": "Light Showers Expected",
            "condition_hi": "हल्की बौछारें संभावित",
            "irrigation_advice_en": "Delay scheduled irrigation. Wait to observe actual rainfall before watering.",
            "irrigation_advice_hi": "निर्धारित सिंचाई को स्थगित करें। सिंचाई करने से पहले वास्तविक वर्षा का अवलोकन करें।"
        },
        {
            "day": "Day 5",
            "temp": "31°C",
            "condition_en": "Thunderstorm & Rain",
            "condition_hi": "गर्जना के साथ वर्षा",
            "irrigation_advice_en": "Do not irrigate today. Ensure proper drainage in fields to avoid waterlogging.",
            "irrigation_advice_hi": "आज सिंचाई बिल्कुल न करें। जलभराव से बचने के लिए खेतों में जल निकासी की उचित व्यवस्था सुनिश्चित करें।"
        }
    ]
}


# 2. Tool Functions

def get_mandi_prices(crop_name: str) -> Dict[str, Any]:
    """
    Fetches mandi price details for a given crop name (Mustard, Wheat, Guar).
    Returns a dictionary with prices and trends, handling multilingual labels.
    """
    crop_cleaned = crop_name.strip().lower()
    
    # Simple mapping logic to catch variations
    target_crop = None
    if "mustard" in crop_cleaned or "sarson" in crop_cleaned or "सरसों" in crop_cleaned:
        target_crop = "mustard"
    elif "wheat" in crop_cleaned or "gehun" in crop_cleaned or "gehoon" in crop_cleaned or "गेहूं" in crop_cleaned or "गेहूँ" in crop_cleaned:
        target_crop = "wheat"
    elif "guar" in crop_cleaned or "ग्वार" in crop_cleaned:
        target_crop = "guar"
        
    if target_crop and target_crop in MANDI_PRICES:
        return {
            "status": "success",
            "data": MANDI_PRICES[target_crop]
        }
    else:
        return {
            "status": "error",
            "message_en": f"Sorry, crop '{crop_name}' is not in our active Rajasthan tracker. Try Mustard, Wheat, or Guar.",
            "message_hi": f"क्षमा करें, फसल '{crop_name}' हमारे सक्रिय राजस्थान ट्रैकर में नहीं है। कृपया सरसों, गेहूं या ग्वार आज़माएं।"
        }


def check_scheme_eligibility(land_size: float) -> Dict[str, Any]:
    """
    Checks eligible government schemes based on the farmer's landholding size (in hectares).
    """
    eligible = []
    for scheme in SCHEMES:
        if land_size <= scheme["max_land_hectares"]:
            eligible.append(scheme)
            
    return {
        "land_size_queried": land_size,
        "eligible_count": len(eligible),
        "schemes": eligible
    }


def get_weather_forecast() -> Dict[str, Any]:
    """
    Returns the hardcoded 5-day irrigation-specific weather forecast for Bharatpur, Rajasthan.
    """
    return WEATHER_FORECAST
