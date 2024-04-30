/*
 * Author: inazo
 * Youtube Channel: https://youtube.com/@kanjian_fr
 * GitHub: https://github.com/inaz0/flipperZero/tree/main/scripts/
 * 
 * Le moteur JS utilisé : https://github.com/cesanta/mjs
 * Inspiration of code: https://github.com/jetblk/Flipper-Zero-JavaScript/blob/main/Scripts/CVE-2024-1086.js
 * https://github.com/jamisonderek/flipper-zero-tutorials/blob/main/js/badusb/badusbdemo.js
 */
let badusb = require("badusb");
let dialog = require("dialog");

//-- On set le layout du clavier super important !
let layout = "us-US";


// Setup BadUSB connection
badusb.setup({ vid: 0x046d, pid: 0xc33f, mfr_name: "Logitech, Inc", prod_name: "Keyboard", layout_path: "/ext/badusb/assets/layouts/" + layout + ".kl" });
print("Waiting for connection");
while (!badusb.isConnected()) {
    delay(1000);
}


// ************
// Show a dialog to pause execution until ready
dialog.message("Test badUSB via JS Script", "Press OK to start");


print("Overture du site kanjian.fr");
delay(500);
badusb.press("GUI", "r");
delay(500);

badusb.print("zzz");
badusb.press("SHIFT",",");
badusb.print("youtube");
badusb.press("SHIFT",",");
badusb.print("co;>");
badusb.press("CTRL","ALT","0");
badusb.print("kqnjiqn8fr>");
badusb.press("SHIFT","m");
// not working code
/*
for(let i=0;i<256;i++){	

	badusb.print(""+String.fromCharCode(i)+"");	
}
*/

// end of not working code

//-- only for the video
let arobase = chr(64);

badusb.print("sub8confir;qtion=");
badusb.press("SHIFT","1");

badusb.press("ENTER");

delay(500);


//-- On sort du mode "clavier"
badusb.quit();

print("Script Complete.");
