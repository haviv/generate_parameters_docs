# Process Run Time Out Minutes

**Technical Name:** ProccessRunTimeOutMintues

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ProccessRunTimeOutMintues` parameter determines the maximum duration a process can run before timing out. It applies to various automation and integration processes within the Pathlock Cloud GRC platform, ensuring that long-running processes do not consume system resources indefinitely.

**Business Impact:**

Setting an appropriate timeout value can prevent system overload and ensure that automated tasks complete within a reasonable time frame. An optimal value helps maintain the efficiency of the GRC operations, avoiding unnecessary delays in workflows and ensuring system stability.

**Technical Impact when configured:**

When the `ProccessRunTimeOutMintues` is configured correctly, it helps in resource management by terminating processes that exceed the specified timeout period. This can prevent potential system hang-ups or crashes caused by processes that become unresponsive or consume excessive resources.

**Examples Scenario:**

- **Mass Data Uploads:** During a mass data upload process, if the upload exceeds the defined timeout, it will be terminated to prevent it from affecting other system operations.
- **Automated Compliance Checks:** In automated compliance checks, if the process takes longer than the specified timeout, it will be stopped to allow other checks to proceed without delay.

**Related Settings:**

- `CommonSettings.Default.RunProccessOutProccess`
- `CommonSettings.Default.PTDM_WorkerProcessPath`

**Applicable Workflows Actions:** 

**Best Practices:** Configure the `ProccessRunTimeOutMintues` to a value that suits your organization’s workflow and system capabilities. Avoid setting it too high to prevent unresponsive processes from consuming system resources for extended periods, or too low which might terminate processes before completing useful work.