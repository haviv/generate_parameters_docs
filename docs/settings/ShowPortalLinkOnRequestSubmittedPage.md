# Show Portal Link On Request Submitted Page

**Technical Name:** ShowPortalLinkOnRequestSubmittedPage

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of portal links on the request submitted confirmation page. When enabled, users will see links to either start a new request or view their open requests, directly from the confirmation page after submitting a request.

**Business Impact:**

Enabling this parameter enhances the user experience by providing quick and easy navigation options, reducing the effort needed to initiate new requests or check the status of existing ones. This can lead to increased user engagement and efficiency in managing requests within the Pathlock Cloud GRC platform.

**Technical Impact when configured:**

- **Enabled:** Displays 'New Request' and 'Open Requests' links on the request submitted page.
- **Disabled:** These links will not be shown, and users may need to navigate through the menu to start a new request or view open requests.

**Examples Scenario:**

1. **User Submission Feedback Loop:** After submitting a request for accessing a new system, a user sees the link to 'Open Requests'. They can immediately click on this to monitor the approval process of their just submitted request, or use the 'New Request' link if they realize another request is necessary.

**Related Settings:** 

- ShowNewRequestLinkOnRequestSubmittedPage
- ShowOpenRequestsLink

**Best Practices:** 

- **Configure when** you have a high volume of users who frequently submit requests, and would benefit from streamlined navigation.
- **Avoid when** minimalistic UI is preferred, or if it's essential to guide users through a more thorough review process before starting new requests.