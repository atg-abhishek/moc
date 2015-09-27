//
//  ViewController.swift
//  NymiPay
//
//  Created by Heng Wang on 2015-09-26.
//  Copyright © 2015 Heng Wang. All rights reserved.
//

import UIKit
import Alamofire


class ViewController: UIViewController {

  override func viewDidLoad() {
    super.viewDidLoad()
    // Do any additional setup after loading the view, typically from a nib.
  }

  override func didReceiveMemoryWarning() {
    super.didReceiveMemoryWarning()
    // Dispose of any resources that can be recreated.
  }

  
  @IBAction func sendRequest(sender: AnyObject) {
    
    let parameters = [
      "hello": "bar",
    ]
    
    Alamofire.request(.POST, "http://localhost:5000/test", parameters: parameters).responseString { response in
      print(response.2.value)
    }
 }

}

