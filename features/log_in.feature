Feature: The reimbursement site has a log in feature
  Scenario Outline: The log in feature allows correct credentials
    Given: The user is on the log in page
    When: The user inputs correct <usr> and <pw>
    When: The user clicks Submit
    Then: The user is taken to the form submission page

    Examples:
    | usr | pw |
    | syensa@rcc.com | kcocaeP776|
    | tistea@rcc.com | ArtisanalCheese469|
    | mannh@rcc.com  | CatchingAllThatRye394|

  Scenario Outline: The log in feature rejects incorrect credentials
    Given: The user is on the log in page
    When: The user inputs incorrect <usr> and <pw>
    When: The user clicks Submit
    Then: The user is not taken to the form submission page

    Examples:
    | usr | pw |
    | syensa@rcc.com | kcocaeP766 |
    | username | password |
    | eesdesdesdesrdc | okboomer |
    | | |