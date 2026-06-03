import pandas as pd

df = pd.read_csv("day_10/security_log.csv")

# how many failures?
failures = df[df["status"] == "failed"]
print(f"Failures: {len(failures)}")
# what percent are failures?
print(f"{len(failures)/len(df)*100}%")
# how many attempts are failutes?
print(f"Total Failed Attempts: {failures["attempts"].sum()/df["attempts"].sum()*100:.2f}%")

# which username has the most failed attempts?
print(failures.groupby("username")["attempts"].sum().idxmax())
# how many failures does that user have?
print(failures.groupby("username")["attempts"].sum().max())

# which IP address is behind the most failures?
print(failures.groupby("ip_address")["attempts"].sum().idxmax())
# what country is that IP from?
print(failures.groupby("country")["attempts"].sum().idxmax())