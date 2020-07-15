#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main(dict):
    count=0
    name=dict.get('name')
    Cmail=dict.get('email')
    resumeLink= dict.get('resume')
    mno=dict.get('mno')
    Cand=""+Cmail
    a1=int(dict.get('a1'))
    a2=int(dict.get('a2'))
    a3=int(dict.get('a3'))
    a4=int(dict.get('a4'))
    a5=int(dict.get('a5'))
    if a1==4:
        count=count+1
    if a2==4:
        count=count+1
    if a3==1:
        count=count+1
    if a4==4:
        count=count+1
    if a5==3:
        count=count+1

    #return {"message": a5}
    from_addr = "recrot.ai.recruiter@gmail.com"
    to_addr = "prateekc231@gmail.com"
    msg = MIMEMultipart()
    msg['From']=from_addr
    msg['To']= to_addr
    msg['subject']="Selected Candidate"
    body= 'Hello HR, We have selected ' + name + ' for Personal Interview round. The Recrot has given '+ name + ' a ' + str(count) + ' star rating on the scale of 1 to 5. ' +'Please contact '+ name +' through Email:- ' + Cmail +' and Resume: '+ resumeLink 
    #body= 'Hello ' + name +', Thank you for taking the time to talk to us about the web developer position. You have successfully Completed the basic questionnaire and assessment, It was a pleasure getting to meet you and we think that you’d be a good fit for this role, You will he hearing from our HR executive Soon for the further interview, Also, feel free to reach out if you have any questions, email us at,'+ from_addr + ' Regards!!'
    msg.attach(MIMEText(body,'plain'))
    email = "recrot.ai.recruiter@gmail.com"
    password = "RecRot@bot_ai"
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)
    text=msg.as_string()
    Cmsg = MIMEMultipart()
    Cmsg['From']=from_addr
    Cmsg['To']= Cand
    Cmsg['subject']="Interview for Web Developer Position"
    Cbody= 'Hello ' + name +', Thank you for taking the time to talk to us about the web developer position. You have successfully Completed the basic questionnaire and assessment, It was a pleasure getting to meet you and we think that you’d be a good fit for this role, You will he hearing from our HR executive Soon for the further interview, Also, feel free to reach out if you have any questions, email us at, '+ from_addr + ' Regards!!'
    Cmsg.attach(MIMEText(Cbody,'plain'))
    Ctext=Cmsg.as_string()
    Rmsg = MIMEMultipart()
    Rmsg['From']=from_addr
    Rmsg['To']= Cand
    Rmsg['subject']="Update on your application for web developer position: Not Shortlisted for Interview Round"
    Rbody=' We thank you for your Application , We appreaciate the efforts you had put behind the entire process and we hope you had learnt a lot during the whole exercise. However, we regret to inform you that your application is NOT SHORTLISTED for the Interview round.Wish you all the best for opportunities ahead! Regards.'
    Rmsg.attach(MIMEText(Rbody,'plain'))
    Rtext=Rmsg.as_string()
    #return {"message": body}
    if count>=3:
        mail.sendmail(from_addr,to_addr,text)
        mail.sendmail(from_addr,Cmail,Ctext)        
    else:
        mail.sendmail(from_addr,Cmail,Rtext)
    mail.quit()
    return {"message": a5}
	
