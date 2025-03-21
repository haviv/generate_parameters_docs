# Active Directory Additional User Attributes

**Technical Name:** ActiveDirectoryAdditionalUserAttributes

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ActiveDirectoryAdditionalUserAttributes` parameter is used to specify additional user attributes that need to be loaded or queried from the Active Directory during synchronization processes or user management operations. These attributes can include but are not limited to, alternate contact numbers, physical office details, postal information, and profile paths.

**Business Impact:**

Configuring additional user attributes allows for a more comprehensive user profile within the Pathlock Cloud GRC platform. This enhanced user information can improve security and compliance management, by allowing for more detailed user profiling and segmentation, which can be particularly useful in access control and regulatory compliance scenarios.

**Technical Impact when configured:**

When additional user attributes are configured, the Active Directory connector will fetch these specified fields during user information synchronization. This can lead to more data being processed and stored, potentially affecting synchronization performance and data storage requirements. However, it significantly enhances the ability to apply granular security and compliance controls based on extended user profile information.

**Example Scenario:**

A company needs to ensure that every user within their GRC platform has their office location (physicalDeliveryOfficeName) and emergency contact numbers (otherMobile, otherPager) available for quick access in case of an on-site incident. By configuring the `ActiveDirectoryAdditionalUserAttributes` parameter to include these fields, the company can automate the collection of this information from their Active Directory, streamlining emergency preparedness and response strategies.

**Related Settings:**

- EmployeeNaturalKeyColumn
- EmployeeAlternativeKeyColumn

**Best Practices:** configure when detailed user profiling and segmentation are required for enhanced security and compliance needs. Avoid extensive use of additional attributes unnecessary for your organization's GRC requirements to prevent performance degradation and excessive data storage.