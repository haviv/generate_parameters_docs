# Sampling Rate For Inbox

**Technical Name:** SamplingRateForInbox

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Sampling Rate For Inbox parameter determines the frequency at which items are sampled or selected for review in the workflow inbox of the Pathlock Cloud GRC platform. It is instrumental in managing the flow of tasks and ensuring that the review process is both efficient and manageable by adjusting the volume of items presented for action.

**Business Impact:**

Adjusting the Sampling Rate for Inbox directly affects the operational efficiency and effectiveness of review processes within an organization's GRC (Governance, Risk Management, and Compliance) strategies. By effectively managing this parameter, businesses can balance the need for thorough review against the resource constraints, ensuring that critical compliance and risk management tasks are prioritized and addressed in a timely manner.

**Technical Impact when configured:**

- **Performance:** Modifying this parameter can impact the system's performance, especially if a very high sampling rate is chosen, potentially leading to increased load times.
- **Workflow Execution:** The rate at which items are brought forward for review can speed up or slow down, affecting how quickly tasks are completed and decisions are made.

**Examples Scenario:**

- **High-Risk Industries:** In sectors such as finance or healthcare where compliance and risk management are critical, setting a higher sampling rate ensures more frequent reviews, minimizing the risk of overlooking critical issues.
- **Resource-Constrained Periods:** During times when staffing is limited or there are high volumes of data to process, reducing the sampling rate can help in managing workflow loads without overwhelming the staff or delaying other processes.

**Related Settings:**

- `ReviewDefaultApprovalGroupTypeId`

**Best Practices:** 

- **Configure when:** It's essential to adjust the sampling rate according to the current business demands, compliance requirements, and available resources. For example, increase the rate during audit preparation periods or when introducing new regulations.
- **Avoid when:** Do not set the sampling to its extremes (either too high or too low) during normal operational periods to prevent system performance issues or backlog of tasks.