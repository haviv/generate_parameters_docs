# Unique Portal Link Validity In Minutes

**Technical Name:** UniquePortalLinkValidityInMinutes

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter defines the validity period, in minutes, for unique portal links generated for actions such as password recovery. Once the set time has elapsed, the link becomes invalid, ensuring a higher level of security by limiting the time window during which a link can be used.

**Business Impact:**

Setting an appropriate validity period for unique portal links is crucial to secure sensitive operations such as password recovery. A too-short validity period could inconvenience users by not providing enough time to access the link and complete the necessary action. Conversely, a too-long validity period could increase security risks by allowing potential unauthorized access if the link is intercepted.

**Technical Impact when configured:**

Configuring this parameter correctly ensures that links for password recovery and possibly other sensitive actions are only active for a designated period, enhancing security by reducing the risk of unauthorized access.

**Examples Scenario:**

Considering a scenario where an organization has determined that links should remain valid for only 15 minutes to balance security needs with user convenience. By setting `UniquePortalLinkValidityInMinutes` to 15, any unique link generated for password recovery will automatically expire after this period, encouraging users to act promptly and reducing the window of opportunity for unauthorized access if the email containing the link is compromised.

**Related Settings:** 

**Best Practices:** configure when establishing or reviewing security policies for access management. Avoid long validity periods to minimize security risks. Consider user experience and feedback to set a reasonable time frame that accommodates user needs while maintaining security integrity.