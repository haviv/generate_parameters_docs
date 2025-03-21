# Target System Logon System

**Technical Name:** TargetSystemLogonSystemId

**Category:** Configuration

**Default Value:** None

**Impact Level:** High

**Description:**

The `TargetSystemLogonSystemId` parameter is designed for specifying the target system's identifier for logon procedures. This identifier is used to configure and manage logon settings within Pathlock's cloud GRC platform, ensuring secure and compliant access control.

**Business Impact:**

Setting the correct `TargetSystemLogonSystemId` is critical for maintaining robust security measures. It ensures that users are logging into the correct system with the right credentials, preventing unauthorized access and potential compliance violations.

**Technical Impact when configured:**

When configured, the `TargetSystemLogonSystemId` directly impacts the logon sequence by defining which system credentials are used for authentication. This plays a key role in secure access management, supporting compliance with security policies and regulations.

**Examples Scenario:**

- **Scenario 1:** An organization needs to ensure that users are authenticated against a specific HR management system for sensitive operations. By setting the `TargetSystemLogonSystemId` to that HR system's unique identifier, they can enforce this requirement.

**Related Settings:** None

**Best Practices:** 

- **Configure when:** You have multiple target systems, and there's a need to specify which system users should authenticate against.
- **Avoid when:** There's only one system or no need for differentiated logon configurations.