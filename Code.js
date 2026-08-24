const dataArray =[];

function myFunction() {
  // initialize
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const cell = sheet.getCurrentCell();
  const row = cell.getRow();
  //Browser.msgBox(cell.getValue()); 

  /** Status 
   */  
  sheet.getRange(row, 2).setValue("Awaiting Response")


  /** Liason 
   * 
   * Button to retrieve name
   * 
   * */ 
  const ui = SpreadsheetApp.getUi();

  const response = ui.prompt(
    'Name of User Required',
    'Please enter your first name:',
    ui.ButtonSet.OK_CANCEL
  );
  
  const buttonClicked = response.getSelectedButton();
  const userInputText = response.getResponseText();
  if (buttonClicked == ui.Button.OK) {
    ui.alert('Howdy ' + userInputText + '!');
  }

  sheet.getRange(row, 3).setValue(userInputText);


  /** Date
   * 
   * Insert formatted Date
   * 
   */
  const tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  const timeZone = Session.getScriptTimeZone();
  const formattedDate = Utilities.formatDate(tomorrow, timeZone, "MM/dd/yyyy"); 
  sheet.getRange(row, 4).setValue(formattedDate);
  
  /** Contact Name(s)
   * 
   * 
   * 
   */
  const contact = sheet.getRange(row, 5).getValue();
  const fullNames = contact.split("\n");
  const firstNames = [];
  for (let i = 0; i < fullNames.length; i++) {
    let firstName = "";
    for (let j = 0; j < fullNames[i].length; j++) {
      if (fullNames[i][j] == " ") {
        break;
      }
      firstName += fullNames[i][j];
    }
    firstNames.push(firstName);
  }

  let referName;
  if (firstNames.length > 2) {
    referName = sheet.getRange(row, 1).getValue() + " Team";
  }
  else if (firstNames.length == 2) {
    referName = firstNames[0] + " and " + firstNames[1];
  }
  else {
    referName = firstNames[0];
  }

  /** Email(s)
   * 
   * 
   */
  emailValue = sheet.getRange(row, 6).getValue();
  const emails = contact.split("\n");
  
  /** Object
   * 
   * 
   */
  const dataInfo = {
    companyName: sheet.getRange(row, 1).getValue(),
    status: "Awaiting Response",
    user: userInputText,
    date: formattedDate,
    contactNames: firstNames,
    referContact: referName
  };

  const jsonString = JSON.stringify(dataInfo, null, 2);
  Logger.log(jsonString);
}
