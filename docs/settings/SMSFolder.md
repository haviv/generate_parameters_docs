# SMS Folder

**Technical Name:** SMSFolder

**Category:** Configuration

**Default Value:** Not provided in the code references.

**Impact Level:** Medium

**Description:** The SMSFolder parameter is used in the context of sending SMS messages as part of automated workflows, specifically when creating new user accounts. It is likely used to specify configurations or templates related to the SMS content or routing.

**Business Impact:** Adequately configuring the SMSFolder parameter ensures that SMS notifications related to new user account creation are correctly dispatched. This can improve the user onboarding experience, enhance security by promptly notifying users of account details, and ensure compliance by keeping users informed.

**Technical Impact when configured:** When correctly configured, the SMSFolder parameter influences how SMS messages are generated and sent in the system. This might include specifying a directory that contains SMS message templates or configuration files that dictate how messages are formatted and processed.

**Example Scenario:** An organization requires that each new user receives a welcome SMS message with login credentials upon account creation. The SMSFolder parameter would be configured to point towards the necessary templates or configurations to ensure this message is dispatched correctly.

**Related Settings:** No directly related settings were identified in the provided code references.

**Best Practices:** configure when initiating workflows that involve SMS communication to ensure messages are correctly formatted and dispatched. Avoid misconfiguration as it could lead to failure in sending critical notifications.