# My Requests Portal Show Last Top Requests

**Technical Name:** MyRequestsPortalShowLastTopRequests

**Category:** Configuration

**Default Value:** Not provided in the given references

**Impact Level:** Medium

**Description:**

This parameter controls the visibility and number of recent requests displayed in the My Requests Portal of the Pathlock GRC platform. It enables the customization of the request history for a more tailored user experience, focusing on the most relevant or recent workflow actions.

**Business Impact:**

Optimizing this parameter can significantly enhance user navigation and efficiency by prioritizing access to recent or critical workflow requests. It aids in streamlining the review and management process of governance, risk, and compliance (GRC) tasks by focusing user attention on current priorities.

**Technical Impact when configured:**

Adjusting this parameter impacts the user interface by altering the volume and presentation of displayed requests within the My Requests Portal, potentially influencing load times and user experience based on the volume of data presented.

**Examples Scenario:**

An organization adjusts this parameter to show only the last 50 requests in the My Requests Portal to ensure that users are not overwhelmed by older, less relevant requests. This helps focus on current tasks and improves the decision-making process for risk and compliance management.

**Related Settings:** 

- MaxRecordsForExcelSheetBuffer

**Best Practices:** configure when, avoid when 

- **Configure when:** You need to tailor the user experience for efficiency and focus, especially in environments with high volumes of workflow requests.
- **Avoid when:** There is a need for users to have comprehensive access to all historical requests without filters, which might be pertinent in audit scenarios or when performing thorough compliance checks.