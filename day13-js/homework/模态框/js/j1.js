//获取dom元素 1.获取事件源
var oBtn = document.getElementById('btn');
//创建弹出模态框的相关DOM对象
var oDiv = document.createElement('div');
var oP = document.createElement('p');
var oSpan = document.createElement('span');


// 设置属性
oDiv.id = 'box';
oP.id = 'content';
oP.innerHTML = "<div style='width:100%;height:100%;overflow: scroll'><h1>小米商城用户协议</h1><br>版本日期：2018年12月18日<br>《小米商城用户协议》（以下简称“本协议”）是您（或称“用户”，指注册、登录、使用、浏览小米商城的个人或组织）与小米科技有限责任公司（平台运营主体）及其关联公司（包括但不限于小米通讯技术有限公司，以下简称“小米”）及其合作单位（包括但不限于第三方商家）之间关于小米商城网站（域名为www.mi.com，简称本网站）与小米产品、程序及服务所订立的协议。小米和合作单位分别就您在本网站接受服务的过程中享受的权利和承担的义务，与您签订本协议，并独立向您承担责任，互不承担保证、连带或共同责任等。<br><br>小米在此特别提醒用户认真阅读 、充分理解---本协议中各条款。您对本协议的接受即自愿接受全部条款的约束，请您务必审慎阅读、充分理解各条款内容，特别是免除或者限制责任的条款、法律适用和争议解决条款，尤此类条款将以加粗的形式提示您注意。如您同意本协议并完成全部注册程序，即表示您已充分阅读、理解并接受本协议的全部内容，并与小米达成一致，成为小米商城平台用户。阅读本协议的过程中，如果您不同意本协议或其中任何条款约定，您应立即停止注册程序。<br><br>一、协议范围<br>1.1【主体范围】<br>小米商城平台运营主体为小米科技有限责任公司，自营商品的销售主体以小米商城网站页面公示的证照信息为准（包括但不限于小米通讯技术有限公司）。本协议项下，小米商城平台运营主体可能根据平台业务调整而发生变更，变更后的小米商城平台运营主体与您共同履行本协议并向您提供服务，小米商城平台运营主体的变更不会影响您本协议项下的权益。<br><br>1.2【协议补充】<br>小米隐私政策（http://www.mi.com/about/new-privacy/）、小米帐号使用协议均为本协议不可分割的一部分，与本协议具有同等法律效力。<br><br>考虑到互联网业务的高速发展，本协议条款并不能完整覆盖您与小米的所有权利和义务，也不能保证完全符合发展的需求。小米商城平台的法律声明、隐私政策、平台规范、规则、通知、公告、操作规则、帮助文档、温馨提示等均为本协议的补充协议，与本协议不可分割且具有同等法律效力。如您使用本平台服务，视为您同意上述补充协议。<br><br>二、小米帐号申请与使用<br>2.1【小米帐号使用协议】<br>如您登陆小米商城，仍需注册有小米帐号。您对小米帐号的申请、使用等行为应符合小米帐号使用协议及小米不时修订并公布的规范。<br><br>2.2【用户资格】<br>在您开始注册程序使用本平台服务前，您应当具备中华人民共和国法律规定的与您行为相适应的民事行为能力。若您不具备前述与您行为相适应的民事行为能力，则您应当在您的监护人的参与下使用本款软件，您及您的监护人应依照法律规定承担因此而导致的一切后果。您帐户下的操作行为，代表您本人；如需代表特定的单位在小米商城平台购买商品或享受服务，您须按照小米的要求提供该单位相关的证件材料及授权材料。<br><br>此外，您还需确保您不是任何国家、国际组织或者地域实施的贸易限制、制裁或其他法律、规则限制的对象，否则您可能无法正常注册及使用小米商城平台服务。<br><br>三、平台服务与规范<br>（一）购买商品<br>3.1.1小米商城平台上的产品和服务由小米科技有限责任公司或其关联公司或第三方商家经营。第三方商家商品的经营主体以页面公示的商家信息为准。为方便表述，商品及服务的经营主体以下统称为“销售商”。对于明确标明为第三方商家提供的商品，开具发票、发货配送、售后服务均由用户所选购商品的商家提供，平台将不承担前述义务及责任，法律、行政法规另有规定除外。<br><br>3.1.2【合同订立】您理解并同意：小米商城平台上展示的商品及其价格、规格等信息仅供您参考，您下单时须确认订单具体内容，确认无误后可提交订单。您在小米商城平台上提交订单并付清全款后，方视为您与销售商之间就您已付款的商品建立了合同关系。在销售商与您的买卖合同成立之前，您与小米均有权取消相关产品的订单。<br><br>3.1.3【先款后货条款】您理解并同意：本平台实行先付款后发货的方式，用户及时、足额、合法的支付选购商品所需的款项是合同成立及生效的条件，也是销售商给用户发货的前提。您未能以合理的方式或在指定时间完成付款的，视为合同未成立，小米有权取消订单。<br><br>3.1.4【缺货免责条款】小米将尽量满足您的需求，避免您选购的商品无货，但是由于技术障碍以及各类难以控制和避免的因素，销售商无法保证符合您提交的订单中所有要求的商品都有货；如您订购的商品无货，您有权取消订单、解除合同，销售商亦有权取消订单、解除合同，若您已经付款，则为您办理退款。订单取消后，您已支付的款项将退回您的付款账户。您理解并认可，退款时间会因不同支付平台、支付方式等原因而有差异。<br><br>3.1.5【限购条款】您理解并认可，基于商品活动规则预设，如销售商在页面公示某些商品的限购数量，若您拟购买超过限购数量的商品，请您与小米或相关第三方商家联系。对于您已经提交的超过限购数量的订单，销售商有权单方予以取消并解除合同。上述限购数量，除特殊说明外并非仅针对单一帐号，如您在一段时间内通过多个帐号下单，单笔订单数量虽未超过该商品限购数量，但通过收件地址、下单IP地址、联系电话、收货人等判断实际购买人为一人或与您有紧密关联的，且多笔订单合计购买数量超过该商品限购数量的，销售商有权取消相关订单、解除合同，小米有权基于该情形决定是否关闭您在小米的帐户并在一定时间内禁止您在小米网站重新注册帐户。<br><br>3.1.6【禁止恶意购买、代购、转售条款】您的购买行为应当基于真实的消费需求，不得存在对商品及/或服务实施恶意购买、恶意维权等扰乱小米平台正常交易秩序的行为。基于维护小米平台交易秩序及交易安全的需要，小米发现上述情形时可主动执行关闭相关交易订单、解除合同等操作。<br><br>小米着眼于向终端消费者的业务拓展，因此不允许代购销售。代购是指客户的主要或者重要的业务通过购买小米商城平台的商品并将其转手给其直接客户的行为。如果小米发现您有转售从小米商城平台上购买的商品的记录，小米有权不再允许您购买商品，并有可能永久地关闭您在小米的该帐户并在一定时间内禁止您在小米重新注册帐户。此禁止转售条款同样适用于您代表单位通过政企团购方式从小米商城平台团购的商品。因您代售或转售小米商城平台上商品而引发的责任及损失，由您本人承担，与小米无关。<br><br>以下情形，小米均有权认定您可能存在转售目的，小米有权认定该订单为异常订单，在商品妥投前，小米均可取消订单、解除合同，退款至您的支付账户：<br><br>（1）同一用户使用多个小米帐号购买同一商品；<br><br>（2）同一商品被大量购买，订单收货地址、收货人姓名及电话、支付帐号、下单IP地址等相同或近似；<br><br>（3）一人或多人使用多个帐号下单，不支付或者选择延迟发货以占用库存；<br><br>（4）同一用户多次或大量无正当理由，拒绝签收订单商品；<br><br>（5）其他可能被认定为存在转售目的的订单。<br><br>本协议项下，使用同一身份认证信息或经小米排查认定多个小米帐号的实际控制人为同一人的，均视为同一用户。<br><br>3.1.7【价格显示】尽管小米尽最大的努力以确保商品价格的准确性，但是商品价格偶尔会有定价错误。如果某一商品的正确定价高于小米商城网站显示的定价，或者由于系统结算错误导致订单价格有误，小米有权根据具体情况决定,联系您咨询您的意见, 或者取消您的订单、解除合同并通知您。<br><br>3.1.8【退货退赠品条款】您退货时应当将商品本身、配件及赠品一并退回。赠品包括赠送的实物、积分、代金券、优惠券等形式。如您选择不退回赠品，您应当按照小米或销售商的要求按照事先标明的赠品价格支付赠品价款。<br><br>3.1.9【平台信息变化】小米商城平台上的商品/服务宣传内容、参数价格、数量、是否有货等商品/服务信息随时都有可能发生变动，小米商城平台不作特别通知。由于平台上的商品/服务信息数量极其庞大，虽然小米商城平台会尽最大努力保证您所浏览商品/服务信息的准确性，但由于众所周知的互联网技术因素等客观原因存在，平台显示的信息可能会有一定的滞后性或差错，对此情形您表示知悉并理解，并同意不追究小米商城平台的违约或侵权责任；如您发现商品/服务信息错误的或有疑问的，请您不要提交订单或接受服务，并在第一时间告诉小米商城平台。<br><br>3.1.10【促销活动说明】小米商城会开展各种形式的促销活动，您仅能在活动有效期内参与活动，才可按照活动规则享受相应优惠。<br><br>3.1.11 订单无论因任何原因取消后，您购买货品所使用的F码（产品购买资格）、支付货款时使用的优惠券等因已经使用而无效，不再退返至您的帐户。关于优惠券是否因使用而无效，如商城有特殊规则，则按照商城的特殊规则处理。<br><br>3.1.12您有权在小米平台提供的评价系统中对您购买的商品或服务进行评价。您的所有评价行为应遵守小米平台规则的相关规定，评价内容应当客观真实，不应包含任何污言秽语、色情低俗、广告信息及法律法规与本协议列明的其他禁止性信息；您不应以不正当方式帮助他人提升信用或利用评价权利对其他用户或商家实施威胁、敲诈勒索。<br><br>（二）商品物流<br>3.2.1 【收货信息】您下单时须填写您希望购买的商品的收货人、联系方式、收货地址、合同履行方式等内容，您购买的商品将按您所指定的送货地址进行配送。因您变更联系人或相关配送信息而造成的损失由您自行承担。<br><br>3.2.2【送货时间】系统会根据不同订单类型而确定是否推送及显示送货时间，如有显示，则订单信息中列出的送货时间为参考时间，参考时间的计算是根据库存状况、正常的处理过程和送货时间、送货地点的基础上估计得出，不属于承诺到货时间，也不等于实际到货或完成安装时间。您知悉平台上的商品有可能存在缺货，或因缺货造成的产品送达迟延，您理解并接受小米对此不承担任何责任。<br><br>3.2.3 【货物妥投】您购买的商品，小米或第三方商家会通过物流公司把商品送到您所指定的收货地址（配送范围外的除外），请您按照小米的收货流程收取货品；当货品妥投给您、您的家人或您指定的收货人或收货人的代理人，即视为您完成收货，并认可收货商品不存在外观瑕疵、损坏或其他问题，您应对收货人的行为及意思表示的法律后果承担连带责任。如须签字确认，请详细阅读相关条款后再签收。<br><br>3.2.4【信息准确】您应准确地填写自己的真实姓名、送货地址及联系方式。因如下情况造成订单延迟或无法配送的，商家无需承担相关责任，并保留单方取消订单的权利：<br><br>（1） 送货地址、联系方式等信息错误、不存在或不够详细；<br><br>（2）送货人员两次通过预留的收货手机联系，无法接通或无人接听；<br><br>（3）货物送达无人签收，由此造成的重复配送所产生的费用及相关的后果；<br><br>（4）不可抗力，如自然灾害、交通戒严、罢工、骚乱、政府行为、突发战争等。<br><br>（三）商品售后<br>3.3.1【售后服务】本平台上销售的产品，售后服务由该产品的“销售商”或供应商负责。不同类型的产品的售后服务依据其产品性质而不同，您应在购买产品过程中详细注意产品页面的标注或展示内容。<br><br>3.3.2【政企团购售后】您理解并同意：如您系通过小米商城的政企团购代表团购单位在小米商城平台上购买货品，因该货品并非销售于消费者，不适用七天无理由退换货，售后政策以网页上的公示为准。<br><br>3.3.3【售后服务区域】您知悉并同意：小米商城平台的商品仅限于中国大陆销售，故小米自营商品仅在中国大陆地区向您提供售后服务；如您携带在小米商城平台购买的商品出关，小米无义务提供任何协助出关的信息。<br><br>（四）第三方<br>3.4.1【第三方产品责任】除小米之外的其他第三方卖家通过小米平台销售商品、提供服务或软件，小米仅为第三方卖家提供网络平台服务，另外，小米提供连接到关联公司和其他企业网站的链接。小米会尽量进行审核和筛查，但小米对于第三方卖家仅提供互联网平台或推广服务，相应的产品、服务责任由该产品、服务的提供者向用户承担。<br><br>3.4.2【支付方式及责任】您有权选择使用小米提供的支付方式，您理解并确认支付服务由具备合法资质的第三方为用户提供，该等支付服务的使用条件及规范由您与支付服务提供方确定，小米不对该支付服务承担任何责任。<br><br>3.4.3【出口管制】小米有权拒绝向被联合国、美国、欧盟及其他国家的列入黑名单的国家、地区及任何机构或个人发送违禁商品。同时，您不得将任何小米生产或销售的产品用于任何军事用途、支持恐怖主义、核设施、生化武器、导弹、大规模杀伤性武器等。您必须遵守可能对商品、软件、技术及服务所适用的美国或其他国家的所有出口及再出口限制。如果您受制于美国的制裁，或受制于您正在使用的小米服务所在地之国家政府施行的、与美国法律一致的制裁，您有可能无法使用小米提供的服务。<br><br>3.4.4【非小米提供服务】在您未发出明确的服务需求的情形下，小米不会主动以电话或其他形式主动向您提供有偿服务，如您接受上述服务，小米对该服务不承担任何责任。<br><br>3.4.5【不可抗力及第三方原因】小米依照法律规定履行相关义务，但对于下述原因导致的合同履行障碍、履行瑕疵、履行延后或履行内容变更等情形，小米并不承担违约责任：<br><br>（1）因自然灾害、罢工、暴乱、战争、政府行为、司法行政命令等不可抗力因素；<br><br>（2）因电力供应故障、通讯网络故障等公共服务因素或任何由于黑客攻击，电脑病毒的侵入，非法内容信息、骚扰信息的屏蔽，政府管制以及其他任何网络、技术、通信线路、信息安全管理措施等原因造成的服务中断、受阻等不能满足您要求的情形；<br><br>（3）在小米已尽善意管理的情况下，因常规或紧急的设备与系统维护、设备与系统故障、网络信息与数据安全等因素。<br><br>四、用户信息的保护及授权<br>4.1【个人信息保护】<br>4.1.1小米将按照隐私政策（http://www.mi.com/about/new-privacy/）收集、使用、处理您的个人信息。按照适用法律，对于您的个人信息，您享有查询、更正、删除以及注销服务或帐号的权利，请发邮件至privacy@xiaomi.com，具体流程请参见隐私政策。<br><br>4.1.2个人信息在完成收集目的后，小米将停止保留数据，或进行脱敏、去标识化处理。但是按照《中华人民共和国电子商务法》的相关规定，小米应当保存交易信息至交易完成之日起三年，但小米不会再处理您的此部分交易信息，法律、行政法规另有规定除外。<br><br>4.1.3我们不会与小米（及相关关联公司或者相关服务提供的主体）以外的任何公司、组织和个人共享您的个人信息，但以下情况除外：<br><br>（1）事先获得您明确的同意或授权； <br><br>（2）根据适用的法律法规、法律程序的要求、强制性的行政或司法要求所必须的情况下进行提供，包括但不限于有关主管部门按照《电子商务法》要求小米提供有关电子商务数据信息（其中包含部分个人信息）的。<br><br>4.1.4 【微信小程序】在特定场景下用户可以选择用自己已有的微信帐号登录小米商城小程序，用户使用以上帐号登陆并关联小米帐号，小米会获取一些用户在这些平台上的信息。鉴于此，用户在进行以上操作时代表您已同意小米获取其在这些门户网站、社交平台上的信息。<br><br>4.2 【信息的发布】您声明并保证，您对您所发布的信息拥有相应、合法的权利。否则，小米可对您发布的信息依法或依本协议进行删除或屏蔽。<br><br>4.3【禁止性信息】您应当确保您所发布的信息不包含以下内容：<br><br>（1）违反国家法律法规禁止性规定的；<br><br>（2）政治宣传、封建迷信、淫秽、色情、赌博、暴力、恐怖或者教唆犯罪的；<br><br>（3）欺诈、虚假、不准确或存在误导性的；<br><br>（4）侵犯他人知识产权或涉及第三方商业秘密及其他专有权利的；<br><br>（5）侮辱、诽谤、恐吓、涉及他人隐私等侵害他人合法权益的；<br><br>（6）存在可能破坏、篡改、删除、影响小米商城平台任何系统正常运行或未经授权秘密获取小米商城平台及其他用户的数据、个人资料的病毒、木马、爬虫等恶意软件、程序代码的；<br><br>（7）其他违背社会公共利益或公共道德或依据相关小米平台协议、规则的规定不适合在小米商城平台上发布的。 <br><br>4.4 【授权使用】对于您提供、发布及在使用小米商城平台服务中形成的除个人信息外的文字、图片、视频、音频等非个人信息，在法律规定的保护期限内您免费授予小米及其关联公司获得全球排他的许可使用权利及再授权给其他第三方使用并可以自身名义对第三方侵权行为取证及提起诉讼的权利。您同意小米及其关联公司存储、使用、复制、修订、编辑、发布、展示、翻译、分发您的非个人信息或制作其派生作品，并以已知或日后开发的形式、媒体或技术将上述信息纳入其它作品内。<br><br>（为方便您使用小米商城平台等其他相关服务，您授权小米将您在帐户注册和使用小米商城平台服务过程中提供、形成的信息传递给其他相关服务提供者，或从其他相关服务提供者获取您在注册、使用相关服务期间提供、形成的信息。<br><br>4.5【信息发送】您同意，小米拥有通过邮件、短信、电话等形式，向您及您指定的收货人发送订单信息、促销活动、广告或广告链接等告知信息的权利。<br><br>五、变更<br>小米可根据国家法律法规变化及维护交易秩序、保护消费者权益需要，不时修改本协议、补充协议，变更后的协议、补充协议（下称“变更事项”）将通过法定程序并以合理方式通知您。如您对已生效的变更事项仍不同意的，您应当于变更事项确定的生效之日起停止使用小米平台服务，变更事项对您不产生效力；如您在变更事项生效后仍继续使用小米商城平台服务，则视为您同意已生效的变更事项。<br><br>六、终止<br>6.1当您发生以下任一情况时，小米商城平台有权限制您的全部或部分权限（包括但不限于下单、参加促销活动等），取消相关未履行完毕的订单、解除合同，或者注销您的小米帐号：<br><br>（1）通过网络攻击、大量发布广告等行为影响网站正常经营或影响网站为其他用户提供服务；<br><br>（2）多次在评论区或咨询区发布与所售商品或服务无关的信息，或多次恶意进行负面评价，违反平台信用评价制度的；<br><br>（3）通过不正当手段（如外挂工具、网络攻击、盗刷银行卡等方式）或其他违法、侵犯第三人利益的方式谋取利益；<br><br>（4）利用销售方过错或失误进行恶意索赔、投诉达两次或以上，或者无故对销售商或客服人员进行辱骂、人身攻击；<br><br>（5）非因商品/服务质量原因，短期内多次拒收商品或拒绝接受服务；<br><br>（6）通过帐户购物从事索赔或转售业务的（如批发、零售）；<br><br>（7）您提供的订单信息（包括但不限于姓名、电话、身份证号、电子邮箱等）不真实、不准确或不完整；<br><br>（8）您有其他影响平台正常经营秩序或违法行为。<br><br>6.2【帐户终止后处理】如您在小米商城平台的帐户被终止，对于您在帐户有效期间产生的交易订单，小米可通知交易相对方并根据交易相对方的意愿决定是否关闭该等交易订单；如交易相对方要求继续履行的，则您应当就该等交易订单继续履行本协议及交易订单的约定，并承担因此产生的任何损失或增加的任何费用。<br><br>6.3【帐户终止权利终止】一旦您在小米商城平台的帐户被终止，您使用小米商城平台服务的权利即告终止。小米不因终止本协议对您承担任何责任，包括终止您的用户帐户和删除您的用户内容；小米也没有义务向您或第三方提供您使用小米商城平台服务所形成的信息资料。<br><br>七、知识产权<br>7.1【知识产权保护】您使用小米帐号及小米商城平台服务的行为应符合《小米帐号使用协议》等相关协议关于知识产权的约定。<br><br>7.2【知识产权许可】您在使用小米商城平台服务时利用小米帐号发表上传的文字、图片、视频、软件以及表演等原创信息的知识产权归您所有，但是您确认您对该等信息的发表、上传行为视同为对小米非独占地、永久地、不可撤销地授予该等信息相关全部知识产权的使用、复制等权利，并且您同意小米可转授权上述权利。<br><br>7.3【知识产权归属】除非经过小米的在先书面同意，您未获得权利使用小米的任何知识产权。您保证、陈述并承诺您尊重小米的知识产权。您不会以自己名义或促使第三方，也不会同意或放任任何第三方，为了其任何营销、广告、促销或其他目的，在任何法域、以任何方式申请与小米或小米关联公司商标相似的商标、域名、无线网站、互联网搜索词或任何商号、服务标志。如出现上述情况，您须将所有相关权利转让给小米，费用由您承担。您保证、陈述并承诺，不会使用以下名称（包括但不限于 “雷军”、“小米”、“小米有品”、“有品”、“米家有品”、“米联”、 “米吧”、“小米商城”、“小米网”、“红米”、“米兔”、 “米家”、“米世界”、“小米互娱”、“小米科技”、“小米生态链”、“爆米花”、“蜜柚”、“小米之家”、 “新国货”、“小米智能家庭”、“小米应用商店”、“米支付”、“米柚”、“米键”、“Xiaomi”、 “MIUI”、“mitalk”、“mitu”、 “APP.MI.COM”、“MIOS”、“HONGMI”、“mi-world”、“MIPAY”、“Mi·Cloud”，上述品牌的附属标志及图案（包括但不限于          等）作为企业、商户、服务或产品名称的一部分，亦不会使用小米商标或近似商标的知识产权。如因您违反本条款约定而给小米造成损失的，该损失全部由您承担。<br><br>7.4【侵权处理】您在小米商城发布的信息不得侵犯任何第三人的知识产权，未经具有相关所有权人之事先书面同意，您不得以任何方式上传、发布、修改、传播或复制任何受著作权保护的材料、商标或属于其他人的专有信息。如您认为小米商城平台上的商品或其他信息侵犯了您的知识产权，请按照小米商城平台上公布的知识产权保护规则及流程处理。<br><br>八、通知<br>您在注册成为小米商城平台用户，并接受小米商城平台服务时，您应该向小米提供真实有效的联系方式（包括您的电子邮件地址、联系电话、联系地址等），对于联系方式发生变更的，您有义务及时更新有关信息，并保持可被联系的状态。小米向您浏览界面推送的弹窗等通知形式，也作为向您发出的有效通知。<br><br>小米将向您的上述联系方式的其中之一或其中若干向您送达各类通知，而此类通知的内容可能对您的权利义务产生重大的有利或不利影响，请您务必及时关注。<br><br>您应当保证所提供的联系方式是准确、有效的，并进行实时更新。如果因提供的联系方式不确切，或不及时告知变更后的联系方式，使通知无法送达或未及时送达，由您自行承担由此可能产生的法律后果。<br><br>九、法律管辖适用及其他<br>9.1本协议应适用中华人民共和国法律。您因使用小米商城平台服务所产生及与小米商城平台服务有关的争议，由小米与您协商解决。协商不成时，任何一方均可向被告住所地有管辖权的人民法院提起诉讼。<br><br>9.2协议中的某些条款因故无法适用，则本协议的其他条款继续适用且无法适用的条款将会被修改，以便其能够依法适用。<br><br>9.3未明示授权的其他权利仍由小米保留，您在行使这些权利时须另外取得小米的书面许可。小米如果未行使前述任何权利，并不构成对该权利的放弃。</div>";
oSpan.innerHTML = 'X';
oSpan.id = 'span1';

// 追加元素
oDiv.appendChild(oP);
oP.appendChild(oSpan);

// 点击弹出按钮 弹出模态框
oBtn.onclick = function () {
    //动态的添加到body中一个div
    this.parentNode.insertBefore(oDiv, oBtn)

};
// 点击X 关闭模态框
oSpan.onclick = function () {
    // 移除oDiv元素
    oDiv.parentNode.removeChild(oDiv)
};
