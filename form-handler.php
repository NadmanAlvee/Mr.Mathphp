<?php
$name = $_post['name'];
$visitor_email = $_post['email'];
$subject = $_post['subject'];
$massage = $_post['message'];


$email_from = 'info@mrmath.com';

$email_subject = 'New Form Submission';

$email_body = "User Name: $name.n\".
               "User Email: $visitor_email.n\".
                "Subject: $subject.n\".
                 "User Massage: $message.n\";

$to = 'nadmanalvee0585@gmail.com';

$headers = "From: $email_from \r\n";

$headers .= "Reply-To: $visitor_email \r\n";

mail($to,$email_subject,$email_body,$headers);

header("location: contact.html");


?>
