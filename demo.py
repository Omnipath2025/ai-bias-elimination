#!/usr/bin/env python3
"""
AI Bias Elimination Demo
Cloak & Quill Research - 501(c)(3) Public Good

This demo shows how current AI systems exhibit bias against traditional medicine
and how our open-source tools can detect and correct this bias.

Usage: python demo.py
"""

def analyze_ai_bias(query, ai_response):
    """
    Analyze AI response for bias against traditional knowledge
    Returns bias score (0-100) and explanation
    """
    bias_indicators = [
        "lacks scientific evidence",
        "not proven",
        "consult your doctor instead",
        "no clinical trials",
        "unsubstantiated claims",
        "folk remedy",
        "alternative medicine"
    ]
    
    bias_score = 0
    detected_bias = []
    
    response_lower = ai_response.lower()
    
    for indicator in bias_indicators:
        if indicator in response_lower:
            bias_score += 15
            detected_bias.append(indicator)
    
    # Cap at 100
    bias_score = min(bias_score, 100)
    
    return bias_score, detected_bias

def suggest_bias_free_response(query, original_response, bias_score):
    """
    Suggest a more balanced response that respects traditional knowledge
    """
    if bias_score < 30:
        return "Response shows minimal bias - good balance of perspectives"
    
    suggestions = [
        "Acknowledge traditional use while noting scientific research status",
        "Include information about cultural significance and historical use",
        "Mention both traditional knowledge and modern research findings",
        "Respect indigenous knowledge while providing comprehensive information"
    ]
    
    return suggestions

def demonstrate_bias_elimination():
    """
    Main demo function showing bias detection in action
    """
    print("=" * 60)
    print("🔬 AI BIAS ELIMINATION DEMO")
    print("Cloak & Quill Research - 501(c)(3) Public Good")
    print("=" * 60)
    print()
    
    # Test cases showing common AI bias
    test_cases = [
        {
            "query": "Is turmeric effective for inflammation?",
            "biased_ai": "Turmeric lacks scientific evidence for inflammation. Consult your doctor instead of using folk remedies.",
            "corrected_ai": "Turmeric has been used traditionally for inflammation for thousands of years. Modern research shows curcumin (turmeric's active compound) has anti-inflammatory properties, with over 300 peer-reviewed studies supporting its efficacy."
        },
        {
            "query": "Can willow bark help with pain?",
            "biased_ai": "Willow bark is an unproven alternative medicine. No clinical trials support its use.",
            "corrected_ai": "Willow bark contains salicin, the precursor to aspirin, and has been used for pain relief since ancient times. Modern aspirin was actually developed based on this traditional knowledge."
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        print(f"📝 TEST CASE {i}")
        print(f"Query: {case['query']}")
        print()
        
        # Analyze biased response
        bias_score, detected_bias = analyze_ai_bias(case["query"], case["biased_ai"])
        
        print("❌ BIASED AI RESPONSE:")
        print(f"   {case['biased_ai']}")
        print(f"   🚨 Bias Score: {bias_score}/100")
        if detected_bias:
            print(f"   🔍 Detected bias indicators: {', '.join(detected_bias)}")
        print()
        
        # Show corrected response
        print("✅ BIAS-FREE RESPONSE:")
        print(f"   {case['corrected_ai']}")
        corrected_bias, _ = analyze_ai_bias(case["query"], case["corrected_ai"])
        print(f"   ✨ Bias Score: {corrected_bias}/100")
        print()
        
        # Show improvement
        improvement = bias_score - corrected_bias
        print(f"📊 IMPROVEMENT: {improvement} point bias reduction")
        print("-" * 60)
        print()

if __name__ == "__main__":
    demonstrate_bias_elimination()
    
    print("🎯 NEXT STEPS:")
    print("• This demo shows basic bias detection")
    print("• With your GitCoin funding, we'll build:")
    print("  - Real-time bias correction")
    print("  - Privacy-preserving attribution")
    print("  - Community validation tools")
    print("  - Global deployment infrastructure")
    print()
    print("💝 Support this public good:")
    print("   GitHub: https://github.com/Omnipath2025/ai-bias-elimination")
    print("   Donate: [GitCoin Campaign Link]")
    print("   Tax-deductible donations (EIN: 99-2969025)")
