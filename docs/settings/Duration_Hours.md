# Duration Hours

**Technical Name:** Duration_Hours

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Duration Hours parameter specifies the range or limit of hours intended for various scheduling, timeout, or duration-based configurations within the Pathlock Cloud GRC platform. It governs the allowable or expected duration hours for activities or features that rely on time-based settings.

**Business Impact:**

Configuring the Duration Hours parameter affects how long certain operations, requests, or processes can remain active or how frequently they are executed within the GRC environment. Correctly setting this parameter helps in ensuring that the system's performance is optimized and complies with the organization's operational policies and schedules.

**Technical Impact when configured:**

When configured, the Duration Hours parameter directly influences the execution window or lifespan of certain processed tasks or requests. It could determine the authorization request's validity, the frequency of automated assessments or checks, and other time-sensitive operations within the system.

**Examples Scenario:**

- **Automated Compliance Checks:** If Duration Hours is set to 24, automated compliance checks can be scheduled to run every 24 hours. This ensures daily verification of compliance with internal or regulatory standards without manual intervention.
- **Authorization Request Expiry:** In scenarios where authorization requests should not be left open indefinitely, setting a specific Duration Hours value can automatically expire these requests after the set period, enhancing security and efficiency.

**Related Settings:**

- `Duration_Minutes` - For further granular control over time-based configurations, allowing settings to be specified in minutes as well.

**Best Practices:** 

- **Configure when:** Establishing or updating workflow schedules, automation frequencies, or any system configurations requiring precise time-based control.
- **Avoid when:** Insufficient analysis has been conducted on the optimal duration for processes, which could lead to system inefficiencies or failures in meeting business requirements.