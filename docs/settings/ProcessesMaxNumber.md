# Processes Max Number

**Technical Name:** ProcessesMaxNumber

**Category:** Configuration

**Default Value:** Not provided in the given code references.

**Impact Level:** Medium

**Description:**

This parameter sets the maximum number of processes that can run concurrently. Adjusting this parameter can help manage system load and prevent performance degradation due to excessive simultaneous processes.

**Business Impact:**

Adjusting the `ProcessesMaxNumber` can directly impact system responsiveness and operational efficiency. A lower limit may ensure that the system remains responsive but could slow down batch processing tasks. In contrast, a higher limit could expedite batch tasks but at the risk of system stability and responsiveness.

**Technical Impact when configured:**

- **Lower Value:** May improve system stability and responsiveness by reducing load but could slow down operations that require multiple processes.
- **Higher Value:** May speed up operations that involve multiple processes but could impact system stability and responsiveness due to increased load.

**Examples Scenario:**

Suppose an organization experiences peak operational periods during month-end financial closing. Adjusting the `ProcessesMaxNumber` to a higher value during this period can help complete batch processing tasks quicker, albeit with increased monitoring of system performance to preclude potential overload.

**Related Settings:**

- `MaximumLogReadDelay`
- `MaximumNotLogged`

**Best Practices:** 

- **Configure when:** There is a need to manage system responsiveness and operational efficiency, such as during peak operational periods or when executing large batch processes.
- **Avoid when:** The default system configuration adequately supports current operational demands without compromising performance or stability.