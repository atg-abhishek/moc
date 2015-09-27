//
//  ViewController.swift
//  NymiPay
//
//  Created by Heng Wang on 2015-09-26.
//  Copyright © 2015 Heng Wang. All rights reserved.
//

import UIKit
import Alamofire


class ViewController: UIViewController,UITextFieldDelegate {


  @IBOutlet weak var cardName: UITextField!
  
  @IBOutlet weak var cardNumber: UITextField!
  
  @IBOutlet weak var expDate: UITextField!
  
  @IBOutlet weak var securityNumber: UITextField!
  
  var kbHeight: CGFloat!
  
  
  override func viewDidLoad() {
    super.viewDidLoad()
    // Do any additional setup after loading the view, typically from a nib.
    cardName.delegate = self
    cardNumber.delegate = self
    expDate.delegate = self
    securityNumber.delegate = self
    
  }
  
  override func viewWillAppear(animated:Bool) {
    super.viewWillAppear(animated)
    
//    NSNotificationCenter.defaultCenter().addObserver(self, selector: Selector("keyboardWillShow:"), name: UIKeyboardWillShowNotification, object: nil)
//    NSNotificationCenter.defaultCenter().addObserver(self, selector: Selector("keyboardWillHide:"), name: UIKeyboardWillHideNotification, object: nil)
  }
  
  override func viewWillDisappear(animated: Bool) {
    super.viewWillDisappear(animated)
//    NSNotificationCenter.defaultCenter().removeObserver(self)
  }
 
  
  
  func textFieldShouldReturn(textField: UITextField) -> Bool {
    cardName.resignFirstResponder()
    cardNumber.resignFirstResponder()
    expDate.resignFirstResponder()
    securityNumber.resignFirstResponder()
    return true
  }

  override func didReceiveMemoryWarning() {
    super.didReceiveMemoryWarning()
    // Dispose of any resources that can be recreated.
  }
  
  @IBAction func login(sender: AnyObject) {
    
    let parameters = [
      "hello": "bar",
    ]
    
    Alamofire.request(.POST, "http://localhost:5000/test", parameters: parameters).responseString { response in
      print(response.2.value)
    }
    
  }
  
  
}

