**Technical Name:** AuthorizationCertificationByActivitiesIncludeRoleName

**Category:** Audit

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether role names are included in the details when performing authorization reviews by activities within the Pathlock Cloud GRC platform. It specifies if the names of the roles associated with the activities are to be displayed in the audit details, enhancing the clarity and context of the authorization review outputs.

**Business Impact:**

Including role names in authorization reviews by activities can significantly improve the understanding of the access rights and activities being certified. This can help auditors and compliance managers to quickly identify any discrepancies or unauthorized access rights, thereby improving the organization's compliance posture and reducing the risk of security breaches.

**Technical Impact when configured:**

When this parameter is configured to include role names, the output of authorization reviews by activities will contain additional details, specifically the names of roles associated with each activity. This enhancement in detail facilitates more informed decisions during the certification process, as it provides clearer insights into the access context.

**Examples Scenario:**

A compliance manager conducting a quarterly review of user access rights decides to include role names in the authorization review by activities report. By doing so, the manager can easily pinpoint that a user has been wrongly assigned to a high-privilege role, which was not immediately obvious without the role names being displayed. This insight allows for prompt corrective action, thereby avoiding potential security risks.

**Related Settings:**

- `GetDetailsControl` (Related to how details are fetched and displayed in the authorization review interface).

**Best Practices:** Configure when conducting detailed authorization reviews to enhance clarity and understanding of access rights. Avoid when such detailed reporting is not required or could lead to information overload.