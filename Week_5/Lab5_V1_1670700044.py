title_Score = """
======================================================
                Score Summary Program
------------------------------------------------------
"""
print(title_Score)
tamt , tsum = 0,0.0
pamt , psum = 0,0.0
amount = int(input("Enter student amount : "))
score = 0 
for i in range(amount):
    score = float(input(f"Enter Score #{i+1} : "))
    if score >= 0 and score <= 100 :
        tamt = tamt+1
        tsum = tsum + score
        if score >= 50 :
            pamt = pamt+1
            psum = psum + score
print("="*45)
print(f"{'Amount of Scores( 0-100 )':<25} : {tamt}")
print(f"{'Average score ':<25} : {tsum/tamt:0.2f}")
print("="*45)
print(f"{'Total pass student ':<25} : {pamt}")
print(f"{'Average pass score ':<25} : {psum/pamt:0.2f}")
print("="*45)
