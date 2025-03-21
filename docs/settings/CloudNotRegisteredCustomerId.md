# Cloud Not Registered Customer

**Technical Name:** CloudNotRegisteredCustomerId

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:** 

The CloudNotRegisteredCustomerId parameter is utilized to identify customers who have not registered their cloud instances within the Pathlock platform. This particularly pertains to the integration and setup phase of onboarding new customers into the platform, ensuring that their cloud environments can be secured, monitored, and managed effectively within the Pathlock ecosystem.

**Business Impact:**

Not configuring this parameter can lead to unmonitored cloud instances, thereby increasing the potential risk of security breaches. It ensures that all customer cloud environments are accounted for and protected under the Pathlock GRC platform's umbrella, maintaining the integrity and security posture of an organization's digital assets.

**Technical Impact when configured:**

Upon configuration, the CloudNotRegisteredCustomerId parameter enables Pathlock administrators to track and incorporate new customer cloud instances into the platform. This action facilitates the activation of security, compliance, and governance features for those instances, thereby extending the platform’s protective measures and oversight capabilities to cover all customer cloud environments.

**Examples Scenario:**

- A new customer onboarded into the Pathlock platform has parts of their ERP systems hosted on cloud servers not yet registered with Pathlock. By entering their CloudNotRegisteredCustomerId into the system, Pathlock admins can start the process of integrating these cloud instances, ensuring all parts of the customer's ERP system are monitored and protected.

**Related Settings:**

- CustomerProfiles
- CloudSegments
- SystemTypes

**Best Practices:** 
- **Configure when:** immediately upon discovering a customer cloud instance that has not been registered within the Pathlock platform. This ensures no cloud environment goes unmonitored or unprotected.
- **Avoid when:** All customer cloud instances are already registered and monitored within the Pathlock system. Duplicate entries or configuration attempts can lead to unnecessary administrative overhead.