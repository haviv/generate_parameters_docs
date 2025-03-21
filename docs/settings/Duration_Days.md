**Technical Name:** Duration_Days

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Duration_Days parameter specifies the duration in days for various operational timelines within the Pathlock GRC platform. This could range from defining the validity period of authorization requests to setting up review cycles for compliance checks.

**Business Impact:**

Adjusting this parameter can directly influence the agility and responsiveness of governance, risk, and compliance (GRC) processes within an organization. A shorter duration may lead to increased operational overhead but can enhance security and compliance posture by ensuring quicker reactions to changes or review requirements. Conversely, a longer duration might reduce administrative burden but potentially delay the identification or remediation of risks and compliance issues.

**Technical Impact when configured:**

Configuring this parameter impacts the scheduling and expiration of tasks related to compliance, authorization management, and possibly security incident investigations. It can alter how frequently reviews are conducted or how long users have to respond to authorization requests, affecting both the workload of teams and the security posture of the organization.

**Examples Scenario:**

- **Compliance Reviews:** If Duration_Days is set to 7 days, compliance review cycles for certain controls must be completed within a week, ensuring a timely check on compliance posture.
- **Authorization Requests:** Setting Duration_Days to 10 days means any access or permission request must be processed within this timeframe, balancing security considerations with operational efficiency.

**Related Settings:** 

- AuthorizationRequestHeader
- AuthorizationRequestStatus
- AuthorizationRequestText

**Best Practices:** 

- **Configure Duration_Days to a value that reflects the organizational need for agility and responsiveness in GRC processes, balancing the need for prompt actions against the risk of rushed assessments or the operational burden of too-frequent reviews.**
- **Avoid setting durations that do not align with external compliance requirements or internal audit cycles, potentially leading to non-compliance or insufficient audit preparation time.**