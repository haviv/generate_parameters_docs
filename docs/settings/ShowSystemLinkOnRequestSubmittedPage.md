**Show System Link On Request Submitted Page**

**Technical Name:** ShowSystemLinkOnRequestSubmittedPage

**Category:** Configuration

**Default Value:** Not provided

**Impact Level:** Low

**Description:**

The "Show System Link On Request Submitted Page" parameter controls the visibility of system-related links on the page displayed after a request is submitted within the Pathlock Cloud GRC platform.

**Business Impact:**

Enabling this feature enhances user experience by providing direct access to system-specific information or actions immediately after submitting a request. It supports efficient navigation and may reduce the time users spend searching for next steps or related information.

**Technical Impact when configured:**

When enabled, system links (e.g., a link to start a new request or view open requests) are made visible on the request submitted page. This improves the workflow by allowing users to quickly initiate new actions without needing to navigate through the platform menu.

**Examples Scenario:**

- A user submits a security configuration change request. Upon submission, the user is presented with a page that includes a direct link to "View Open Requests" or "Start a New Request," thereby streamlining the process of managing multiple requests.

**Related Settings:**

- ShowNewRequestLinkOnRequestSubmittedPage
- ShowRoleTypeColumn
- ShowCompanyColumn

**Best Practices:** Enable this feature in environments where users are likely to engage in multiple requests within a single session to enhance navigation and improve user satisfaction. Avoid enabling it if the additional links may overwhelm or confuse users, especially in simpler implementations where such shortcuts are not necessary.