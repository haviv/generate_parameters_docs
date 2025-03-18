# Change Documents Show Activity

**Technical Name:** ChangeDocumentsShowActivity

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

The ChangeDocumentsShowActivity parameter controls whether activity descriptions are included in the change document reports within the Pathlock Cloud GRC platform. This setting is crucial for auditing and monitoring changes across the GRC platform, ensuring that administrators and auditors have comprehensive visibility into each action taken on change documents.

**Business Impact:**

Enabling the ChangeDocumentsShowActivity parameter ensures that all changes made within the GRC environment are documented with a detailed activity description. This is vital for maintaining a transparent audit trail, highlighting the importance of each change and its impact on the organization's compliance and risk posture. It facilitates easier audit reporting, enhances security monitoring, and supports compliance with various regulatory standards.

**Technical Impact when configured:**

When configured to include activity descriptions, the system will generate more detailed reports for each change document. These reports will contain not only the basic information about each change but also a descriptive account of the activity performed. This level of detail is instrumental in pinpointing specific changes, understanding the context of each modification, and assessing the implications of these changes on the overall GRC strategy.

**Example Scenario:**

A financial institution uses the Pathlock Cloud GRC platform to manage its compliance with industry regulations. The administrator enables the ChangeDocumentsShowActivity parameter to ensure that all changes to compliance documents are fully documented with activity descriptions. This setting allows for a detailed audit trail, which assists in an external audit where the institution must provide evidence of compliance activities and changes. As a result, the auditors can easily trace each change, understand its purpose, and verify the institution's adherence to regulatory requirements.

**Related Settings:**

- WorkflowApprovalGroupTypeIdForFallback

**Best Practices:** 

- **Configure when:** It is imperative to have a detailed audit trail for regulatory compliance, security monitoring, or to enhance transparency in change management processes.
- **Avoid when:** System performance issues arise due to the extensive logging of detailed activities, or in environments where change volume is low, and such detailed tracking might be overkill.