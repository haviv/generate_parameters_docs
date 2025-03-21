# Schedule Authorization Review Use Recurrence Parameter

**Technical Name:** ScheduleAuthorizationReviewUseRecurrenceParameter

**Category:** Workflow

**Default Value:** Not provided in the code references

**Impact Level:** Medium

**Description:**

The Schedule Authorization Review Use Recurrence Parameter is designed to specify whether authorization reviews within the Pathlock Cloud GRC platform should be executed on a recurring basis. This parameter helps in determining the cycle for re-evaluating and validating the access rights and privileges allotted to users, ensuring continuous compliance and governance.

**Business Impact:**

Enabling recurrence for authorization reviews facilitates regular scrutiny of user permissions, helping organizations maintain stringent security protocols and comply with internal or regulatory standards. It aids in identifying and mitigating potential access risks preemptively, thereby protecting sensitive information and resources.

**Technical Impact when configured:**

When this parameter is configured to enable recurrence, the system automatically schedules subsequent authorization reviews based on the defined frequency. This ensures that authorization reviews are not overlooked and are conducted as part of a routine compliance check.

**Examples Scenario:**

- An organization needs to comply with financial regulations requiring quarterly reviews of user access to their financial systems. By utilizing the Schedule Authorization Review Use Recurrence Parameter, they can ensure that these reviews are automatically set to recur every quarter without manual intervention.

**Related Settings:** Not provided in the code references

**Best Practices:** Configure the Schedule Authorization Review Use Recurrence Parameter to match the organization's compliance requirements and risk management strategies. Avoid setting the recurrence period too short as it may lead to operational inefficiencies, or too long, which may risk non-compliance with regulatory standards.