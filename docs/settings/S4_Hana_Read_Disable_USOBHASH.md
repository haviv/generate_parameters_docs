# S4 Hana Read Disable USOBHASH

**Technical Name:** S4_Hana_Read_Disable_USOBHASH

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

The parameter `S4_Hana_Read_Disable_USOBHASH` is designed to control the read access to the USOBHASH functional module (FM) within the SAP S/4HANA system. It acts as a switch to enable or disable the reading of USOBHASH values, which are crucial for determining the hash values associated with user roles and authorizations.

**Business Impact:**

Enabling this setting can significantly impact how authorization checks are performed, potentially affecting system security and compliance with internal controls. Disabling read access may be required in environments where strict control over authorization-related information is necessary.

**Technical Impact when configured:**

When set to `True`, the system will block read access to the USOBHASH by FM, which could impact applications or services relying on this information for role validation or authorization checks. It may lead to increased security by limiting exposure to sensitive data but could also hinder functionality that depends on this access to operate correctly.

**Examples Scenario:**

Consider a scenario where an organization needs to comply with stringent security regulations that necessitate limiting access to sensitive authorization data. By setting this parameter to `True`, the organization can ensure that unauthorized access to USOBHASH data is prevented, thereby enhancing the security posture and compliance with the regulatory requirements.

**Related Settings:** 

- S4_Hana_Read_USOBHASH_BY_FM

**Best Practices:** configure when you need to increase security and compliance by restricting access to sensitive role and authorization information; avoid when applications or services require access to USOBHASH for legitimate purposes.