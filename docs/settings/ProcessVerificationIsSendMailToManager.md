# Process Verification Is Send Mail To Manager

**Technical Name:** ProcessVerificationIsSendMailToManager

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter controls whether a notification email is sent to managers during the process verification phase in workflow actions. It is part of the Pathlock Cloud GRC's workflow management system, enabling or disabling automated email notifications related to process verifications tasks or outcomes.

**Business Impact:** Enabling this parameter ensures managers are promptly informed about the status of process verifications, which can lead to more efficient oversight, quicker responses to compliance or risk issues, and improved communication within the organization. Disabling it may reduce email clutter but could also risk oversight on critical verification tasks.

**Technical Impact:** when configured, this parameter affects the automated email notifications system. If enabled, it triggers an email to the designated managers whenever a process verification is completed or requires attention. This is aimed at ensuring there is an added layer of oversight by the management on verification processes.

**Examples Scenario:** If an organization wants to ensure that managers are directly notified when their team members complete a significant compliance verification process, this parameter should be activated. It ensures that managers are always in the loop regarding compliance activities, without having to manually check the system for updates.

**Related Settings:** ImportManagersToWFUserGroupDescriptionTemplate

**Best Practices:** 

- **Configure when**: Immediate manager oversight is necessary for process verifications, or in workflows where manager intervention or acknowledgment is a part of the compliance or audit procedures.
  
- **Avoid when**: Managerial oversight is not critical for every step of the process verification, or to reduce email notifications for managers.