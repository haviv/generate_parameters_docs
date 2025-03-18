**Access Certification Wait Processing Message**

**Technical Name:** AccessCertificaiton_WaitProcessingMessage

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AccessCertification_WaitProcessingMessage` parameter is used to customize the message displayed to users during the processing of access certifications in the Pathlock Cloud GRC platform. This message is intended to inform users that their request is being processed and to wait for completion, enhancing user experience by providing clear communication during processes that might take time.

**Business Impact:**

Proper configuration of this parameter enhances user satisfaction by managing expectations during longer processing times for access certifications. It helps in reducing user frustration by providing a clear message that the system is working on their request, potentially reducing the number of support tickets related to access certification delays.

**Technical Impact when configured:**

When this parameter is configured, the specified message is displayed to users during the access certification process. This aids in clear communication with users, especially during processes that are not instantaneous, ensuring users are aware that their actions are being processed.

**Example Scenario:**

Consider a scenario where an organization has implemented a complex access certification process that includes various checks and approvals which might take several minutes to complete. By customizing the `AccessCertification_WaitProcessingMessage` to display a message such as "Your access certification request is being processed, please wait. This may take a few minutes.", users are informed about the ongoing process, leading to a better user experience and reduced user anxiety over the wait time.

**Related Settings:**

- `AuthorizationReviewShowFillEmptyToApprove`
- `AuthorizationReviewShowFillEmptyToDecline`

**Best Practices:** 

- **Configure when:** There is an anticipated delay in the processing of access certifications to manage user expectations effectively.
- **Avoid when:** The access certification process is typically fast, and adding a wait message might unnecessarily alarm the users or imply that the system is slower than it actually is.