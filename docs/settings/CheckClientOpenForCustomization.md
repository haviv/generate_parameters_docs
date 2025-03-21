# Check Client Open For Customization

**Technical Name:** CheckClientOpenForCustomization

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter determines whether a client's settings allow for customization post-implementation. It is utilized to ensure that any modifications to the client's environment are controlled and do not violate established security or governance policies.

**Business Impact:**

Enabling this parameter allows organizations to maintain a balance between flexibility in configuration and adherence to security standards. It prevents unauthorized or accidental changes that could impact the integrity and security of the system, thereby mitigating risks associated with compliance violations.

**Technical Impact when configured:**

When configured, this parameter acts as a safeguard against unintended changes, ensuring that only authorized customizations are made to the client's configurations. It involves checking if the client is open for customization before proceeding with any changes, thereby maintaining system stability and compliance.

**Examples Scenario:**

- **Scenario 1:** A company has completed the implementation of the Pathlock Cloud GRC platform. Post-implementation, the IT department wishes to add extra features or customize settings to fit evolving business needs. Before proceeding, the CheckClientOpenForCustomization parameter would be assessed to ensure these changes are permitted, preventing any unauthorized modifications.

**Related Settings:** 

- `ActiveDirectoryProviderTestAllProperties`

**Best Practices:** 

- **Configure when:** It's essential to have control over who can make changes to the client's settings, especially in environments where security and compliance are paramount.
  
- **Avoid when:** The client's environment requires frequent adjustments, and there are robust processes and checks in place to manage these changes securely.