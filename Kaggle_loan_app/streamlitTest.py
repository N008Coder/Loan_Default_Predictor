from operator import truediv
import streamlit as st

st.title("Loan Default Calculator")

form1=st.sidebar.form(key="abc123")
form1.header("Please enter your information as accurately as possible: ")


var2= form1.selectbox("What is your gender?",["Male", "Female","Joint", "NA"])
var3= form1.selectbox("What region are you based in?",["North","South", "North-East", "Central"])
var6= form1.selectbox("What type of loan?",["type1", "type2","type3"])
var7= form1.selectbox("What is the purpose of the loan?",["p1","p2","p3","p4"])
var10= form1.selectbox("Is the loan business or commercial?",["Business","Commercial"])
var11= form1.number_input("What is the loan amount?")
var15= form1.number_input("What is the length of term?")
var17= form1.selectbox("How would you like to repay your loan?",["Interest Only", "Principle + Interest"])
var19= form1.number_input("What is the value of your property?")
var21= form1.selectbox("What is your occupency type?",["ir","pr","sr"])
var22= form1.selectbox("What is your property secured by?", ["home", "land"])
var24= form1.number_input("What is your income (monthly)?")
var25= form1.selectbox("Where is your credit report coming from?",["EXP","EQUI","CIB","CRIF"])
var26= form1.number_input("What is your credit score?")
var27= form1.selectbox("Where is the credit report coming from for your co-applicant?",["EXP","EQUI","CIB","CRIF"])
var28= form1.selectbox("What age bracket do you fall under?",[">25","25-34","35-44","45-54","55-64","65-74",">74"])

results=[]
results.append([var2,var3,var6,var7,var10,var11,var15,var17,var19,var21,var22,var24,var25,var26,var27,var28])

if form1.form_submit_button("Submit Report"):
   # insert predictor here \/
    st.write(results)

indexa = 0
indexb = 0
indexc = 0
indexd = 0
#approval = predictor 

#if form1.form_submit_button ==True:
#    if approval ==True:
 #       st.write(results)
 #       st.write("Congratulations You've Been Approved!")
  #  else:
   #     while predictor(var1,var2,var3,var4,var5) < .5
    #        var5 += 100
     #       indexa +=1
      #  else:
       #     indexa1 = indexa * 100
        #    st.write(f"Please raise your credit score by {indexa1} to receive approval.")



