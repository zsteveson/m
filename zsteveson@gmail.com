Original Message

Message ID	<f91896bc8b40ad5.4f1bfe8009f69378a8bb44cc02f00e49@mailer.surveygizmo.com>
Created at:	Fri, Dec 1, 2017 at 10:53 AM (Delivered after 1 second)
From:	SurveyGizmo <info@relay.edu>Using SurveyGizmo
To:	zachary.steveson@surveygizmo.com, zsteveson@gmail.com, zsteveson@yahoo.com
Subject:	New Response Notification
SPF:	PASS with IP 146.20.14.105 Learn more
DMARC:	'PASS' Learn more


Download Original	Copy to clipboard	
Delivered-To: zsteveson@gmail.com
Received: by 10.237.46.131 with SMTP id k3csp1289416qtd;
        Fri, 1 Dec 2017 07:53:58 -0800 (PST)
X-Google-Smtp-Source: AGs4zMYLC9ugLA4cZ/nc0l0HYTC7kew4PTyImoomK4v/1X1KXEBCm+4DGAiBf29wvy6jswgBqd8P
X-Received: by 10.200.56.75 with SMTP id r11mr9177022qtb.65.1512143638929;
        Fri, 01 Dec 2017 07:53:58 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1512143638; cv=none;
        d=google.com; s=arc-20160816;
        b=kCt4SxCt2w5BCXFZPTxDUR68jjZGzPgTBSY+eRuQ3OtyKRyR1SH8IDhoB/pvkSM94Q
         AzphafbzwYg9GFmP1Rh0VFJARbgucRDVKjR98PHCwrP0Hom+BETb+bBx/nFIdb9STry2
         S3GOjsXAcmYt/WfpKN7G9zAklH7eUAc383F1d6bZaFB5FsvdFeohichMtNZxT3EybNv0
         HZ2YnYXycuCcuuHVvKBF0GYLac5E54j057OLeG6Gvb85XHb3QvEIITEawkBt6YlVBiyP
         JBqyCiowFyXDgp56hFYsyBizOi0s9F7j0a/vL0JI7Smb3r4Y0goMRkHYfnwtpuAlthCg
         ggPw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=mime-version:list-unsubscribe:message-id:subject:reply-to:from:to
         :date:errors-to:arc-authentication-results;
        bh=6qAMjHJHrz0sta1eAcUwpICB8Lqyp2Hghkk/E0VgCls=;
        b=i12nXg3ri8qq0dAKKchW3pmiGZb/gwW/R/AquXvrkRv+T/RjJB4vOp6M+Ir/malZnw
         AnrZkT/yL2Hq63OOYqj2+YWuPYOwuP2+DxUtCYd540HD6QzWZy6Zyx53xEjDOKIVVZ6B
         F7RXpSccSEwNo+JfBoCuVBUG4dDNyJBy9mH/Rl8leOWe0sFTmOEPjHRt9Kq2GWdG50FV
         pBqSgiQfCJ1TRp4obu53bbGktXvhHykldbdPKTTx3y2qBklRVWnlNkH3UDk7XZ9OOfJZ
         fsPTsFh1/82e6A6S6hbRBoFk5u8U+MPvZ9k77TxP7mQRgU6+Ci8U2+zXwd7zwvEKDCW4
         eyJw==
ARC-Authentication-Results: i=1; mx.google.com;
       spf=pass (google.com: domain of info@relay.edu designates 146.20.14.105 as permitted sender) smtp.mailfrom=info@relay.edu;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=relay.edu
Return-Path: <info@relay.edu>
Received: from rspmtaeast-01.sgizmo.com (rspmtaeast-01.sgizmo.com. [146.20.14.105])
        by mx.google.com with ESMTPS id a34si7068780qte.97.2017.12.01.07.53.58
        for <zsteveson@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Fri, 01 Dec 2017 07:53:58 -0800 (PST)
Received-SPF: pass (google.com: domain of info@relay.edu designates 146.20.14.105 as permitted sender) client-ip=146.20.14.105;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of info@relay.edu designates 146.20.14.105 as permitted sender) smtp.mailfrom=info@relay.edu;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=relay.edu
Received: by rspmtaeast-01.sgizmo.com id h45thc28ip4l for <zsteveson@gmail.com>; Fri, 1 Dec 2017 10:53:58 -0500 (envelope-from <info@relay.edu>)
x-errors-to: mailerrors@sgizmo.com
errors-to: mailerrors@sgizmo.com
Date: Fri, 1 Dec 2017 10:53:57 -0500
Return-Path: info@relay.edu
To: zachary.steveson@surveygizmo.com, zsteveson@gmail.com, zsteveson@yahoo.com
From: SurveyGizmo <info@relay.edu>
Reply-to: No Reply <noreply@surveygizmo.com>
Subject: New Response Notification
Message-ID: <f91896bc8b40ad5.4f1bfe8009f69378a8bb44cc02f00e49@mailer.surveygizmo.com>
X-Priority: 3
X-Mailer: SurveyGizmo
X-Complaints-To: abuse@sgizmo.com
List-Unsubscribe: <unsub-action-4036961-1512143636_5a217b1406f1f2.89574790-2@mailer.surveygizmo.com>
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="b1_f91896bc8b40ad5.4f1bfe8009f69378a8bb44cc02f00e49"

--b1_f91896bc8b40ad5.4f1bfe8009f69378a8bb44cc02f00e49
Content-Type: text/plain; charset = "utf-8"
Content-Transfer-Encoding: 8bit

This is sample text (replace with your own).



Email Uses

You can use email auto-responders to send your survey takers a thank you, a follow up, or a copy of the survey results to yourself. In order to email your customer make sure to ask for their email address somewhere in your survey. Use their email question merge code in the field above "Send Email To: Email Address".



About Merge Codes

You can use Merge Codes to introduce survey values into your email like a word processor mail merge. Use the Insert button to add the merge code wherever your cursor is placed. Use the "Insert All" button to add all questions and merge codes at once for a complete record of the survey. Here is an example :



Thank you for taking time to participate in our survey. We truly value the information you have provided. By participating in this survey, you made your voice heard and are helping shape the future of .

{Thank the participant for their time and let them know what you will do with the information and how it will help you (and them)}



The compiled results of the survey will be detailed in our next newsletter. For your records, your answers are included at the bottom of this email.

{If you plan on sharing the results, tell them how they can get them.}



The winners of the free widget will be notified by email in the next couple days.

{If you have an incentive and the participant must do some additional steps, outline them here}



You can always find us on Facebook or on Twitter.

{Give the participant a way to continue to interact with you}



Thank you again for your time and input,



Your Name





Your Answers:

{Use the Merge Code helper’s 'Insert All Questions' here}


--b1_f91896bc8b40ad5.4f1bfe8009f69378a8bb44cc02f00e49
Content-Type: text/html; charset = "utf-8"
Content-Transfer-Encoding: 8bit

This is sample text (replace with your own).<br />
<br />
<strong>Email Uses</strong><br />
You can use email auto-responders to send your survey takers a thank you, a follow up, or a copy of the survey results to yourself. In order to email your customer make sure to ask for their email address somewhere in your survey. Use their email question merge code in the field above "Send Email To: Email Address".<br />
<br />
<strong>About Merge Codes</strong><br />
You can use Merge Codes to introduce survey values into your email like a word processor mail merge. Use the Insert button to add the merge code wherever your cursor is placed. Use the "Insert All" button to add all questions and merge codes at once for a complete record of the survey. Here is an example :<br />
<br />
Thank you for taking time to participate in our survey. We truly value the information you have provided. By participating in this survey, you made your voice heard and are helping shape the future of .<br />
<i style="color: #999">{Thank the participant for their time and let them know what you will do with the information and how it will help you (and them)}</i><br />
<br />
The compiled results of the survey will be detailed in our next newsletter. For your records, your answers are included at the bottom of this email.<br />
<i style="color: #999">{If you plan on sharing the results, tell them how they can get them.}</i><br />
<br />
The winners of the free widget will be notified by email in the next couple days.<br />
<i style="color: #999">{If you have an incentive and the participant must do some additional steps, outline them here}</i><br />
<br />
You can always find us on Facebook or on Twitter.<br />
<i style="color: #999">{Give the participant a way to continue to interact with you}</i><br />
<br />
Thank you again for your time and input,<br />
<br />
Your Name<br />
<br />
<br />
Your Answers:<br />
<i style="color: #999">{Use the Merge Code helper’s 'Insert All Questions' here}</i>



--b1_f91896bc8b40ad5.4f1bfe8009f69378a8bb44cc02f00e49--