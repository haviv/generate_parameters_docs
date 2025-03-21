**Automatic Workflow SoD Mitigated Fixed Day In Month**

**Technical Name:** AutomaticWorkflowSoDMitigatedFixedDayInMonth

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:** This parameter determines the specific day of the month on which automated workflows related to Segregation of Duties (SoD) are considered mitigated. It is a critical setting for planning and executing SoD mitigation strategies within the Pathlock GRC platform.

**Business Impact:** Configuring this parameter helps organizations to systematically manage and mitigate SoD violations on a fixed schedule, thereby aligning the mitigation process with internal audit cycles or compliance deadlines. It ensures timely action on potential security risks, contributing to a stronger internal control environment.

**Technical Impact when configured:** Once set, this parameter triggers the execution of SoD mitigation workflows automatically on the defined day each month, streamlining the process for managing user access and control violations without manual intervention.

**Examples Scenario:** If the parameter is set to the 15th day of each month, any SoD conflicts identified by the Pathlock platform will automatically initiate mitigation workflows on the 15th day of each month, ensuring consistent and timely resolution of identified risks.

**Related Settings:** 

**Best Practices:** Configure this parameter at the beginning of the implementation of the Pathlock GRC system to align with your organization's internal audit and compliance reporting cycles. Avoid setting this parameter without considering your organization’s specific SoD mitigation requirements and timelines, to ensure that automated workflows are triggered in alignment with the organization's risk management strategy.