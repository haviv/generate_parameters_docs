**Change Documents Read Source Table For More Info**

**Technical Name:** ChangeDocumentsReadSourceTableForMoreInfo

**Category:** Reporting

**Default Value:** "SELECT OpenOn,OpenFor,RequestStatus,form_all,DetailsLink"

**Impact Level:** Medium

**Description:** This parameter allows the customization of queries that read from the source table to provide more detailed information in reporting documents. It helps in tailoring the details visible in workflow reports to include specific fields based on requirements.

**Business Impact:** Adjusting this parameter can significantly affect the information available for audit and compliance reviews. It ensures that reports are comprehensive, focusing on the critical elements that matter most to the business, thereby improving decision-making and oversight.

**Technical Impact when configured:** Modifying this parameter influences how data is fetched and presented in reports. It allows the inclusion of additional fields such as OpenOn, OpenFor, RequestStatus, and others, enhancing the granularity and relevance of report content for users.

**Examples Scenario:** An organization may need to include transaction-specific details in their change document reports to meet compliance requirements. By configuring this parameter, they can include fields like `RequestStatus` and `DetailsLink` in their reports, providing auditors with direct links to transaction records and real-time status updates.

**Related Settings:** WorkflowReportDefaultQuery

**Best Practices:** 

- **configure when** specific reporting requirements are not met by the default settings, such as when there is a need for more detailed audit trails or to fulfill specific compliance requirements.
  
- **avoid when** the default report settings suffice your organization's reporting needs as unnecessary complexity can introduce challenges in report maintenance and performance.