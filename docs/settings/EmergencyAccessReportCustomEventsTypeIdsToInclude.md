# Emergency Access Report Custom Events Type Ids To Include

**Technical Name:** EmergencyAccessReportCustomEventsTypeIdsToInclude

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

This parameter is designed to include specific event type IDs in the emergency access report. It plays a vital role in filtering the events that are critical for auditing purposes, ensuring that only relevant data is presented for review.

**Business Impact:**

Selective inclusion of event IDs into the emergency access report allows for targeted auditing of user activities during emergency access periods. This significantly enhances the organization's ability to detect and respond to unauthorized or inappropriate actions, ensuring compliance with internal security policies and external regulatory requirements.

**Technical Impact when configured:**

When configured, this parameter limits the events reported in the Emergency Access Report to only those that have been specified by the included type IDs. This tailored reporting aids in focusing audit efforts on the most critical and relevant activities, enhancing the efficiency and effectiveness of the audit process.

**Examples Scenario:**

A scenario where this parameter is beneficial is in organizations that operate under strict regulatory compliance requirements. For instance, if only changes to financial records or high-privileged user accounts are considered critical, specifying their event type IDs ensures that the emergency access report focuses only on these activities. This enables auditors to efficiently review and take necessary actions without being overwhelmed by less significant data.

**Related Settings:**

- CompareSoDRisksBasedOnCausingRoles

**Best Practices:** 

- **Configure when:** You need to generate focused and relevant emergency access reports for audit purposes, specifically when dealing with large volumes of user activity data.
  
- **Avoid when:** If the environment does not process a high volume of emergency access events or if indiscriminate reporting is preferred for comprehensive auditing.