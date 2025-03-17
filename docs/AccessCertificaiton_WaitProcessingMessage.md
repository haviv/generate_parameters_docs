# Access Certification Wait Processing Message

**Technical Name:** AccessCertificaiton_WaitProcessingMessage

**Category:** Workflow

**Default Value:** ""

**Impact Level:** Medium

**Description:** This parameter controls the display message to users during the processing wait time in access certification workflows. It improves user experience by providing informative feedback during system operations that require significant processing time.

**Business Impact:** Tailoring the wait processing message can significantly enhance the user experience during access certification processes. By setting an appropriate and informative message, organizations can reduce user frustration and confusion during lengthy processing times, leading to more efficient and user-friendly access certification cycles.

**Technical Impact when configured:** Setting a custom message will replace the default system message during access certification processing times. This allows for a more personalized user interaction, potentially improving user compliance and engagement with the certification process.

**Examples Scenario:**

- **Before Setting a Custom Message:** Users might see a generic or default message such as "Processing..." during long wait times, which may not provide much insight into the operation's progress.
  
- **After Setting a Custom Message:** Users might see "Your access certification is currently being processed. Thank you for your patience!" This provides a clearer expectation and enhances the user experience.

**Related Settings:** Not explicitly mentioned in the provided code snippets, but it may relate to other user interface customization settings within the Pathlock Cloud GRC platform.

**Applicable Workflows Actions:** While specific workflow actions relating to this parameter were not detailed in the provided context, it is applicable to any workflow action within the access certification process that involves significant processing time.

**Best Practices:** 

- **Configure when:**
  - The processing time for access certification is considerably long.
  - There’s a need to enhance user communication and experience during access certification processes.
  
- **Avoid when:**
  - The default system message suffices due to the quick processing times of access certifications.
  - Custom messaging could introduce confusion or misinterpretation of the process status.

**Context:** This parameter is part of the Pathlock Cloud GRC platform's workflow settings, aimed at improving the user experience during access certification processes by allowing for customized processing wait messages.