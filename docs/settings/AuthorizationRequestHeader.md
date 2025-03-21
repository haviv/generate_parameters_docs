**Authorization Request Header**

**Technical Name:** AuthorizationRequestHeader

**Category:** Security

**Default Value:** None

**Impact Level:** High

**Description:**

The Authorization Request Header parameter is used to manage secure access controls across the Pathlock Cloud GRC platform. It ensures that API requests and interactions with various services within the platform are authenticated and authorized adequately, safeguarding sensitive data and operations from unauthorized access.

**Business Impact:**

A correctly configured Authorization Request Header is critical for maintaining the integrity and confidentiality of sensitive compliance, risk management, and security data. It prevents unauthorized access and protects against potential security breaches, contributing to overall organizational compliance and risk mitigation strategies.

**Technical Impact when configured:**

- Ensures secure communication between client applications and the Pathlock Cloud GRC services.
- Facilitates adherence to stringent security policies and compliance requirements by enforcing authentication on API calls and service requests.
- Helps in tracking and auditing access to the system for security and compliance purposes.

**Examples Scenario:**

- **Securing API Access:** When external applications need to access the Pathlock Cloud GRC APIs, the Authorization Request Header must contain a valid security token to authenticate the request, ensuring that only authorized applications can access sensitive information or perform operations.

**Related Settings:** WorkflowApprovalGroup, ProfileTailorSystem, EmailMessageTemplate, Customer, PatternSet, WorkflowCategory

**Best Practices:** 

- **Configure when:** Setting up integration between Pathlock Cloud GRC and other systems or when external applications need to communicate with the Pathlock platform. Ensure that the Authorization Request Header is present and correctly configured on all requests to protect against unauthorized access.
  
- **Avoid when:** If there's no clear requirement for external system integration or if the involved systems do not support header-based authentication, alternative authentication methods should be considered.