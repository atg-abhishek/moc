//
//  NymiHandler.m
//  NymiPay
//
//  Created by Heng Wang on 2015-09-26.
//  Copyright © 2015 Heng Wang. All rights reserved.
//

#import "NymiHandler.h"
//#import "NymiPay-Swift.h"


#define NYMI_API_SERVICE_HOST_IP @"172.20.34.97"
#ifndef NYMI_API_SERVICE_HOST_IP
#error "Please define NAPI_SERVER_IP to  machine running an instance of the napi-service (we'll talk to that server here). Typically this will be your dev box."
#endif


@class AppDelegate;

@interface NymiHandler()

@property (weak, nonatomic) AppDelegate *appDelegate;

@end

@implementation NymiHandler

//@synthesize nymi_api;

- (id)init {
  self = [super init];
  if(self)
  {
    NSString *serverHost = NYMI_API_SERVICE_HOST_IP;
    _nymi_api = [[NymiApi alloc] initWithServer:serverHost];
  }
  
  return self;
}

@end
