import pandas as pd
import random

customers=[]
for i in range(1,101):
    customers.append([i,f"Customer{i}",f"user{i}@mail.com","India"])

policies=[]
for i in range(1,101):
    policies.append([i,i,"Health",random.randint(5000,20000),random.randint(1,10)])

claims=[]
for i in range(1,201):
    claims.append([i,random.randint(1,100),random.randint(1000,15000),"Approved"])

pd.DataFrame(customers,columns=["customer_id","name","email","country"]).to_csv("../csv/customers.csv",index=False)
pd.DataFrame(policies,columns=["policy_id","customer_id","policy_type","premium_amount","risk_score"]).to_csv("../csv/policies.csv",index=False)
pd.DataFrame(claims,columns=["claim_id","policy_id","claim_amount","claim_status"]).to_csv("../csv/claims.csv",index=False)

print("Generated insurance CSV files.")
