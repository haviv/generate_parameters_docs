**Technical Name:** ShowOpenRequestsLinkOnRequestSubmittedPage

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The ShowOpenRequestsLinkOnRequestSubmittedPage parameter controls the visibility of a link to open requests on the page displayed after a request has been submitted. This feature aims to enhance user navigation by allowing users to easily access and monitor the status of their open requests.

**Business Impact:**

Enabling this parameter improves the user experience by providing a direct path to review and manage existing requests without navigating away from the current workflow. This can lead to increased efficiency in request management and monitoring, contributing to better compliance and oversight in governance, risk management, and compliance (GRC) processes.

**Technical Impact when configured:**

When configured to display the link, users will see an option to view open requests immediately after submitting a new request. This facilitates quick transitions between submitting a request and managing ongoing ones, potentially speeding up the process of request review and approval.

**Examples Scenario:**

After submitting a new access request in the Pathlock Cloud GRC platform, a user is brought to a confirmation page. With ShowOpenRequestsLinkOnRequestSubmittedPage enabled, the user sees a "View Open Requests" link on this page. By clicking this link, the user can immediately see all their pending requests, including the one just submitted, and follow up on any necessary actions without having to navigate through multiple pages.

**Related Settings:**

**Best Practices:** Configure this parameter to enhance navigation and user experience, particularly in environments where users frequently submit and manage multiple requests. Avoid enabling it in scenarios where the focus should remain on singular task completion without diversion.