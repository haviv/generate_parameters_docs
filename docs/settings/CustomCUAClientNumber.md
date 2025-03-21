# Custom Central User Administration Client Number

**Technical Name:** CustomCUAClientNumber

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Custom Central User Administration (CUA) Client Number parameter is used to specify a unique identifier for clients within the Central User Administration setup in SAP systems. This parameter ensures that user management and security protocols are properly aligned across different systems managed by Pathlock's Cloud GRC platform.

**Business Impact:**

Setting the CustomCUAClientNumber correctly is crucial for businesses that utilize centralized user management across multiple systems. Incorrect configuration may lead to unauthorized access, ineffective user management, and potential compliance violations.

**Technical Impact when configured:**

When configured correctly, this parameter allows for seamless integration and management of user roles and access rights across SAP systems in a CUA environment. It ensures that user data and permissions are accurately synchronized, enhancing both security and operational efficiency.

**Examples Scenario:**

A company uses Pathlock's Cloud GRC platform to manage their SAP environments. They operate with multiple SAP client numbers across different systems. By setting the CustomCUAClientNumber to their specific client number, they can centralize user administration tasks, ensuring consistent access control and compliance with internal policies.

**Related Settings:**

- CommonSettings.Default.EnableCUA
- Context.CurrentSettings.DisableCua

**Best Practices:** configure when a centralized approach for user administration across multiple SAP systems is required, avoid when each system should be managed independently due to specific compliance or business requirements.