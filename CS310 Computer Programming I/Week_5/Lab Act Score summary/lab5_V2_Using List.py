title_Score = """
======================================================
                Score Summary Program
------------------------------------------------------
"""
print(title_Score)
tscore = []
pscore = []

amount = int(input("Enter student amount : "))
score = 0 
for i in range(amount):
    score = float(input(f"Enter Score #{i+1} : "))
    if score >= 0 and score <= 100 :
        tscore.append(score)
        if score >= 50 :
            pscore.append(score)
print("="*45)
print(f"{'Amount of Scores( 0-100 )':<25} : {len(tscore)}")
print(f"{'Average score ':<25} : {sum(tscore)/len(tscore):0.2f}")
print("="*45)
print(f"{'Amount of Scores( 0-100 )':<25} : {len(pscore)}")
print(f"{'Average score ':<25} : {sum(pscore)/len(pscore):0.2f}")
print("="*45)