#import <Foundation/Foundation.h>

@class NymiBand;

typedef void (^AgreementCallback)(NSString* led_pattern);
typedef void (^ProvisionCallback)(NSString* led_pattern, NymiBand* new_provision);
	// Provisioning can fail. NymiBand* will be nil in this instance.

typedef void (^NANumDetectedChangedCallback)(int);
typedef void (^NAPresenceChangeCallback)(NymiBand*);

@interface NymiApi : NSObject
	+(id) connect:(NSString*)ws_server_host;
	-(id) initWithServer: (NSString*) ws_server_host;
	-(id) initWithServer: (NSString*) ws_server_host andPort:(int) port;

	@property (readonly) NSURL* server_url;
	// identifies the object
	// (even if an application has multiple instances connected to the same 
	//  backend; those instances are all logically equivalent).

	-(void) enableProvisioning:(AgreementCallback) agreement_callback;
	-(void) acceptProvision:(NSString*) led_pattern;
	-(void) acceptProvision:(NSString*) led_pattern withCallback:(ProvisionCallback) callback;
	-(void) rejectProvision:(NSString*) led_pattern;
	-(void) disableProvisioning;

	@property (readonly) int numDetectedBands;
	@property (readonly) NSArray* provisionedBands;
	// array of NymiBand*, one for each band provisioned with the server.

	-(void) setNumDetectedChangedCallback:(NANumDetectedChangedCallback) cb;
	-(void) setPresenceChangeCallback:(NAPresenceChangeCallback) presence_cb;
	// Called whenever any provisioned band's presence changes (appears/disappers)

	// TODO
	// -(id) pause;
	// -(id) resume;
	// (needed for application backgrounding ... )
@end


@interface NymiBand : NSObject
	@property (readonly) NymiApi*  originating_connection;

	@property (readonly) NSString* name;
	@property (readonly) BOOL present;

	-(void) setPresenceChangeCallback:(NAPresenceChangeCallback) presence_changed;
	// callback is fired only when this band's presence changes.
@end
