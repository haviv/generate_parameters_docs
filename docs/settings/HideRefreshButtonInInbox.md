# Hide Refresh Button In Inbox

**Technical Name:** HideRefreshButtonInInbox

**Category:** Configuration

**Default Value:**

**Impact Level:** Low

**Description:**

The HideRefreshButtonInInbox parameter controls the visibility of the refresh button within the inbox on the Pathlock Cloud GRC platform. This can be used to streamline the user interface and reduce distractions or accidental data refreshes by users during critical workflow management activities.

**Business Impact:**

Adjusting the visibility of the refresh button can affect the efficiency of review processes by reducing the risk of accidental data refreshes which might interrupt the workflow or force the user to lose their place. This is particularly relevant in environments where precise control over workflow activities is necessary.

**Technical Impact when configured:**

When the HideRefreshButtonInInbox parameter is configured to hide the refresh button, users will no longer be able to manually refresh their inbox view by clicking a dedicated button. This may reduce inadvertent refreshes but could also necessitate users to rely on alternative methods for refreshing their view, such as browser reloads or navigation reentries.

**Examples Scenario:**

- **Context:** An analyst regularly reviews security alerts in their Pathlock inbox. Accidental refreshes have led to losing track of their review process.
  
  **Before Configuration:** The refresh button is readily available, leading to frequent unintentional inbox refreshes.
  
  **After Configuration:** The refresh button is hidden, reducing disruptions and accidental loss of place during the review process.

**Related Settings:**

- Display.Visible
- openRequestsInNewWindow.Visible

**Best Practices:** 

- **Configure when:** A streamlined workflow is essential, and the risk of accidental data refresh needs minimization. Suitable for environments where users work on critical tasks that require maintaining a state or focus without interruptions.
  
- **Avoid when:** Users rely heavily on the ability to quickly and frequently refresh their data or in dynamic work environments where the most current information is continually required.