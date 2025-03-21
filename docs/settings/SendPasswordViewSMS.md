# Send Password View SMS

**Technical Name:** SendPasswordViewSMS

**Category:** User Management

**Default Value:** False

**Impact Level:** High

**Description:**

The Send Password View SMS parameter is a configuration setting used within the Pathlock Cloud GRC platform to control whether users receive their passwords via SMS after their account creation or authorization adjustments. This parameter is particularly relevant in workflows where security and accessibility are prioritized.

**Business Impact:**

Activating this feature ensures that users can securely and immediately access their accounts without delay, enhancing user experience and security protocol compliance. It is particularly vital for new user onboarding and in scenarios where users are granted new authorizations that require quick access.

**Technical Impact when configured:**

When enabled, this parameter triggers the sending of a password via SMS to the user's registered mobile number upon the execution of applicable workflow actions such as account creation or authorization updates. This process is critical for ensuring timely access while maintaining security standards.

**Examples Scenario:**

1. **New User Onboarding:** A new employee is added to the system, and an SMS is automatically sent to them with their password, allowing them immediate access to necessary systems and applications.
2. **Authorization Update:** A current employee is granted access to a new system or application, and an SMS is sent to them with the new system password, ensuring they can use the new permissions without delay.

**Related Settings:** None

**Applicable Workflows Actions:** 

- ApplyAuthorizationAction
- CreateNewUser

**Best Practices:** 

- **Configure when:** Immediate user access is critical, and there's a reliable SMS delivery mechanism.
- **Avoid when:** Users do not have access to a secure mobile device or when SMS delivery is unreliable.