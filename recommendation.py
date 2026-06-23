def get_recommendations(interest):
    recommendations = {
        "ai": [
            "Introduction to AI",
            "Generative AI Basics",
            "AI for Beginners"
        ],
        "machine learning": [
            "Machine Learning Fundamentals",
            "Supervised Learning",
            "Scikit-Learn Essentials"
        ],
        "data science": [
            "Data Analysis with Python",
            "Statistics for Data Science",
            "Data Visualization"
        ],
        "web development": [
            "HTML & CSS",
            "JavaScript Basics",
            "Full Stack Development"
        ]
    }

    return recommendations.get(interest.lower())


print("=" * 40)
print("   AI Course Recommendation System")
print("=" * 40)

print("\nAvailable Interests:")
print("1. AI")
print("2. Machine Learning")
print("3. Data Science")
print("4. Web Development")

interest = input("\nEnter your interest: ")

courses = get_recommendations(interest)

if courses:
    print("\nRecommended Courses:")
    for course in courses:
        print(f"- {course}")
else:
    print("\nSorry! No recommendations found.")
    print("Please choose from:")
    print("AI, Machine Learning, Data Science, Web Development")