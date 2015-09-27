//
//  NymiHandlerViewController.m
//  NymiPay
//
//  Created by Heng Wang on 2015-09-27.
//  Copyright © 2015 Heng Wang. All rights reserved.
//

#import "NymiHandlerViewController.h"

@interface NymiHandlerViewController ()

#define NYMI_API_SERVICE_HOST_IP @"172.20.34.97"
#ifndef NYMI_API_SERVICE_HOST_IP
#error "Please define NAPI_SERVER_IP to  machine running an instance of the napi-service (we'll talk to that server here). Typically this will be your dev box."
#endif

@end

@class AppDelegate;

@interface NymiHandlerViewController()

@property (weak, nonatomic) AppDelegate *appDelegate;

@end

@implementation NymiHandlerViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    NSString *serverHost = NYMI_API_SERVICE_HOST_IP;
    _nymi_api = [[NymiApi alloc] initWithServer:serverHost];


    // ========= NYMI API Instance =========
    // The NymiApi class is our entry point to doing things with Nymi bands.
    // In this application, the instance lives with the AppDelegate.
//    _appDelegate = [[UIApplication sharedApplication] delegate];
//    if(!_appDelegate.nymi_api){
//      NSLog(@"Uh-oh something went wrong with initializing the API");
//      return;
//    }

}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
