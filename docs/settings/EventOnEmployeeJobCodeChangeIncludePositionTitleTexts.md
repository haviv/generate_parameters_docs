**Event On Employee Job Code Change Include Position Title Texts**

**Technical Name:** EventOnEmployeeJobCodeChangeIncludePositionTitleTexts

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter determines whether the position title texts should be included in events triggered by changes in an employee's job code.

**Business Impact:**

Including position titles in job code change events enhances visibility into workforce movements and role evolutions, aiding in accurate and comprehensive audit trails. This promotes better governance and compliance by ensuring that all role changes, and the context around them, are captured and can be reported on.

**Technical Impact when configured:**

When enabled, the system will append position title texts to the job code change events captured. This ensures that audit logs and alerts not only capture the change but also provide a clear understanding of the nature of the role transition, by including the position title text.

**Examples Scenario:**

An employee is promoted from a "Junior Analyst" position to a "Senior Analyst." With this setting enabled, the event log will not only indicate the job code change but will also include the transition from "Junior Analyst" to "Senior Analyst" titles, providing a complete view of the promotion.

**Related Settings:** 

- ShowForgetPasswordLinkInLoginPage (This setting, while in a different category, also pertains to system configurations aimed at enhancing user experience and security.)

**Best Practices:** configure when

- Full transparency and detailed audit trails are necessary for compliance and governance.
- It is important to track not just the fact of a job code change, but also the qualitative nature of such changes through position titles.

avoid when

- Minimalism in logging is required due to storage constraints or for simplicity.
- The inclusion of position titles does not serve an additional business or compliance need.