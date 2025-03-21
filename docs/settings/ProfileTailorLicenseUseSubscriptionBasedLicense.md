# Pathlock License Use Subscription Based License

**Technical Name:** ProfileTailorLicenseUseSubscriptionBasedLicense

**Category:** Configuration

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

The `ProfileTailorLicenseUseSubscriptionBasedLicense` parameter controls whether the Pathlock GRC application should validate the product key as part of a subscription-based licensing model. This is important for organizations to manage and maintain compliance with the software licensing agreements.

**Business Impact:**

Ensuring that the software is used within the licensing terms helps prevent legal and financial repercussions associated with software piracy or misuse. It aids organizations in staying compliant with Pathlock's licensing model, avoiding potential license overuse charges.

**Technical Impact when configured:**

When enabled, it requires the system to validate the product key against Pathlock's licensing server or mechanism, ensuring that the usage complies with the purchased subscription. It may also influence system behavior such as access to updates, support, and functionality available within the GRC platform.

**Examples Scenario:**

A company has recently migrated its GRC processes to Pathlock and needs to ensure that its use of the software complies with the agreed subscription terms. By enabling the `ProfileTailorLicenseUseSubscriptionBasedLicense` parameter, they can automate the verification of their software's product key, thus ensuring compliance and avoiding any unauthorized usage.

**Related Settings:** ReportFilterUseWideRoleFilter

**Best Practices:** 

- **Configure when:** You are setting up the Pathlock system for the first time or when transitioning to a subscription-based license.
- **Avoid when:** Your organization does not use Pathlock under a subscription license model or if you are using a perpetual license that does not require frequent validation.