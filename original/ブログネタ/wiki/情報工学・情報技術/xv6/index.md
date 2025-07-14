---
title: 'xv6'
description: 'xv6'
date: '2025-01-03'
categories: []
weight: 999
math: true
draft: true
---

- アーキテクチャ
  - インテル系
    - x86
  - Arm
  - RISC-V
- CPU
  - 
- OS
  - Windows
  - Mac
  - Linux
  - Unix
- ディストリビューション (Linux のみ)
- 

## コンピュータの動作原理

- 基礎的な CPU の構造
  - ALU (Arithmetic Logic Unit): 算術論理演算装置
  - ノイマン型コンピュータ
    - 命令メモリ (ROM・ROM32K): 16 bit の機械語で書かれた命令を保存したメモリ
    - データメモリ (RAM・Memory): プログラムで扱うデータを格納したメモリ
    - CPU: 中央演算処理装置
- アセンブリ
  - スタックマシン
    - 実行可能ファイルのフォーマット
      ``` 
      .text
      .data
      ```
    - どうメモリに配置されるか
- コンパイラ

## OS の仕組み
- OS に必要な機能
  - **メモリ管理**
    - 仮想メモリ
    - メモリ保護
  - **マルチタスク・プロセス管理**
    - マルチプレクス
    - マルチスレッド
    - マルチプロセッサ対応
  - **ファイルシステム管理**
  - **API 提供**
    - システムコール
  - ハードウェア管理・制御
  - ネットワーク
    - NIC ドライバ + TCP/IP: http://dsas.blog.klab.org/archives/2020-04/xv6-net.html
  - ユーザインタフェース
- プロセッサの歴史
  - 川合秀実氏著「30日でできる！OS自作入門」が出版された2006年頃まで
  - それ以降
    - マルチプロセッサ化
    - 32 bit から 64 bit への移行
    - ファームウェアの変遷
      - レガシー BIOS から UEFI への移行: ブートローダの作成方法が変わってしまう
- OS をサポートする CPU の機能
  - プロセッサ実行モードの分割
  - ぺージングテーブル
  - 割り込み機能
  - アトミック命令
- BIOS
  - マザーボードに搭載されているプログラムで、基本的なハードウェアの制御を行っており、OS をインストールしなくても画面に入ることができる
  - BIOS
    - レガシー BIOS ともいう
    - 各記憶装置の最初の512バイト(MBR)を読み出して、その領域の末尾に、起動可能かどうかを示すマジックナンバー(0x55, 0xAA)があるかを確認して、それが存在すればそのデータを0x7c00番地に配置して、そこに実行を引き渡します。
      - OS の作り方

    - HDD/SSD の先頭セクタに 

    - MBR (Master Boot Record) 形式で初期化されたディスクからのみブートできる
      - MBR ディスクの構造
      
        - MBR セクター
          - 容量は 512 バイトで、マスターブートコード (446 バイト) とディスクパーティションテーブル (DPT、64 バイト) とブートサイン (2 バイト) で構成される
        - パーティション
      - 最大 4 つのパーティションを作成できる
        - DPT の容量が 64 バイトと少なく、パーティション情報が 16 バイト必要なため、\\( 64 / 16 = 4 \\) つまでの制限があるらしい
        - プライマリーパーティションを拡張パーティションにしてロジカルパーティションを作成すれば 4 つより多くのパーティションを作成できるらしい
      - 最大容量の制限が2TB
        - ハードディスク容量の情報が 32 bit で管理されており、1 セクタ 512 バイト (ハードディスクはセクタ単位で管理している) であることから、2^32 * 2^9 バイト = 2 TB までしか認識できないらしい
        - 4Kn (4Kネイティブ) セクタを使用している場合は 2^32 * 2^12 = 16 TB まで認識できるらしい
  - UEFI

    - 各記憶装置上のファイルシステムを読み、仕様書で規程されているパスに置かれている実行ファイルをロードするようになっています。

      - x86_64アーキテクチャにおいては/EFI/BOOT/BOOTx64.EFI
    - MBR (Master Boot Record) 形式で初期化されたディスクからのみブートできる
    
      - 先頭の 512 一応 MBR
      - GPT ディスクの構造
        - 保護MBR
          - GPTディスクの一番先にあるセクターもMBRセクターになり、MBRディスクのと異なり、GPTディスクの保護MBRは、MBRディスクのみにサポートするツールがGPTパーティションを破壊することを防ぐ機能を発揮しています。
        - プライマリーGPTヘッダー
          - GPTディスクの2番目のセクターには、プライマリーGUIDパーティションテーブルヘッダーが保存されています。プライマリーGUIDパーティションテーブルヘッダーは、パーティションテーブルからなるパーティションエントリーの場所とサイズ情報と、巡回冗長検査（CRC32）のチェックサムが内包されています。
        - パーティションエントリー
          - 三番目のセクターから30-40番目のセクター（合計32個セクター）の部分はパーティションエントリーとなります。一般的には、GPTディスクに無制限なパーティションが作成可能ですが、オペレーティングシステムによってパーティション数が制限される可能性があります。例えば、Windows環境下でパーティションエントリーのサイズは128バイトなので、パーティションを最大128（32*512/128）個作成することができます。これはMBRディスクと比べる最もの違いです。
        - パーティション
          - GPTディスクにプライマリーパーティションを無制限に作成することができるので、拡張パーティション、又はロジカルパーティションが存在しません
        - バックアップパーティションエントリー/プライマリーGPTヘッダー

- プロセッサエミュレーター

  - qemuの-nographic

  - ``` 
    qemu-system-riscv64 -machine virt -bios none -kernel kernel/kernel -m 128M -smp 3 -nographic -global virtio-mmio.force-legacy=false -drive file=fs.img,if=none,format=raw,id=x0 -device virtio-blk-device,drive=x0,bus=virtio-mmio-bus.0 -S -gdb tcp::26000
    ```

  - 引数

    - `-machine`
    - `-bios`
    - `-kernel`
    - `-m`: メモリ
    - `-smp`: プロセッサ数
    - `-drive file=fs.img,if=none,format=raw,id=x0`
    - `-device virtio-blk-device,drive=x0,bus=virtio-mmio-bus.0`
    - ` -S`
    - `-gdb tcp::26000`

## xv6

### xv6 の仕様 (事前に知っておくと便利な項目を抜粋)

- xv6 はそうするかわりに，そのマシンは 128 MB の RAM を持つと決め打ちします。
- プロセスは 64 個までと決め打ち

### 起動時
- `start.c` -> `main.c`
- ブートローダ
-  `main` 関数 (`kernel/main.c`)
  - 物理メモリのアロケータ
    - ``` 
      kinit();         // physical page allocator
      ```
    - `kinit` 関数: 物理メモリのアロケータを初期化する
  - ページテーブル
    - ``` 
      kvminit();       // create kernel page table
      kvminithart();   // turn on paging
      ```
    - `kvminit` 関数では `satp` レジスタに 0 が書き込まれているので、仮想アドレスは有効ではなく物理アドレスに領域を確保する
    - `kvminithart` 関数で `satp` レジスタにアドレスが書き込まれるので、ページングテーブルを利用した仮想アドレスが有効になる
  
  - 残り
  
    ``` 
        procinit();      // process table
        trapinit();      // trap vectors
        trapinithart();  // install kernel trap vector
        plicinit();      // set up interrupt controller
        plicinithart();  // ask PLIC for device interrupts
        binit();         // buffer cache
        iinit();         // inode table
        fileinit();      // file table
        virtio_disk_init(); // emulated hard disk
        userinit();      // first user process
    ```

### トラップ時

- 出てくるレジスタ

  - `satp` レジスタ: ページングテーブルのアドレスを入れる
  - `sepc` レジスタ: トラップが発生したら，RISC-V はプログラムカウンタをここに退避しま
    す (pc は，直後に stvec の値で上書きされてしまうからです)．sret (return
    from trap) 命令は sepc を pc にコピーします．カーネルは，sepc に書き込
    むことで，sret の飛び先を制御します．
  - `stvec` レジスタ: トラップベクタの命令列
- ハードウェア処理
  - トラップ実行時
    - 処理内容
      - トラップがデバイスの割込で, sstatus の SIE ビットがゼロだったら，続く
        処理は行わない．
      - SIE をゼロにして割込を無効化する．
      - pc を sepc にコピーする.
      - 現在のモード（ユーザもしくはスーパーバイザ）を，sstatus の SPP ビットにセーブする．
      - 割込の原因を表すように scause をセットする．
      - スーパーバイザモードにする．
      - stvec を pc にコピーする.
      - 新しい pc で実行を開始する.
    - CPU は次のことはしてくれません．よって，カーネルが，必要に応じて上記の処理を行わなくてはいけません． 
        - カーネルページテーブルの切り替え
        - カーネルのスタックへの切り替え
        - pc 以外のレジスタの退避
    
  - `sret` (return from trap) 命令:  `pc` レジスタに `sepc` レジスタの値をコピーする
- カーネル空間からのトラップ

    - 初期状態
      - `satp` レジスタ: ページングテーブルのアドレスを入れる
      - `sscratch` レジスタ: プロセス固有の trapframe (kernel/proc.h:44) をセット
      - `stvec` レジスタ: `kernelvec` のアドレス
      - が指すトラップベクタの命令列
    - ハードウェア処理
      - `pc` レジスタに `stvec` レジスタの値をコピー: ハードウェア処理後、`kernelvec` 関数の最初から実行する
    - `kernelvec` 関数の処理前半
    - `kerneltrap` 関数
    - `kernelvec` 関数の処理後半
- ユーザ空間からのトラップ

  - 初期状態
    - `satp` レジスタ: プロセスのページングテーブルのアドレスが入っている
    - `sscratch` レジスタ: プロセス固有の trapframe (kernel/proc.h:44) をセット
    - `stvec` レジスタ: `uservec` のアドレス
    - が指すトラップベクタの命令列
  - ハードウェア処理
  - `uservec` 関数 (`kernel/trampoline.S`)
    - `satp` レジスタにカーネルのページングテーブルのアドレス値をコピーする
      - `uservec` が入っている `trampoline` 部分の仮想メモリのアドレスはプロセスとカーネルで共通なので、`satp` レジスタの値を変えても `uservec` 関数をそのまま実行できる
    - 最後に `usertrap` 関数を実行する
  - `usertrap` 関数 
    - 最後に `usertrapret` 関数を実行する
  - `usertrapret` 関数
    - 最後に `userret`  関数を実行する
  - `userret`  関数 (`kernel/trampoline.S`)
- タイマ割り込み

### 並行性制御テクニック
- タイマ割り込みによるマルチプレクス
  ```mermaid
  sequenceDiagram
  Title: タイマ割り込みによるマルチプレクス
  
  box プロセスA
      actor au as プロセスA(ユーザー)
      actor ak as プロセスA(カーネル)
  end
  actor sch as スケジューラ
  box プロセスB
      actor bk as プロセスB(カーネル)
      actor bu as プロセスB(ユーザー)
  end
  
  activate au
  au ->> ak: uservec 実行<br>プロセス A の<br>実行情報を保存
  deactivate au
  activate ak
  note left of au: 割り込み
  note left of ak: yield 関数内<br>プロセス A の<br>ロック取得
  note left of ak: yield 関数内<br>sched 関数実行
  ak ->> sch: sched 関数内<br>swtch
  deactivate ak
  activate sch
  note right of sch: プロセス A<br>ロック解放
  note left of sch: プロセス B の<br>ロック取得
  note left of sch: scheduler 関数内<br>プロセス B の<br>swtch 実行
  sch ->> bk: swtch
  deactivate sch
  activate bk
  note right of bk: プロセス B の<br>ロック解放
  bk ->> bu: usertrapret<br>プロセス B の<br>実行情報を復元
  deactivate bk
  activate bu
  note right of bu: プロセス B の<br>続きのプログラムを<br>そのまま実行する
  bu ->> bk: uservec 実行<br>プロセス B の<br>実行情報を保存
  deactivate bu
  activate bk
  note right of bu: 割り込み
  note right of bk: yield 関数内<br>プロセス B の<br>ロック取得
  note right of bk: yield 関数内<br>sched 関数実行
  bk ->> sch: sched 関数内<br>swtch
  deactivate bk
  activate sch
  note left of sch: プロセス B<br>ロック解放
  note right of sch: プロセス A<br>ロック取得
  note right of sch: scheduler 関数内<br>プロセス A の<br>swtch 実行
  sch ->> ak: swtch
  deactivate sch
  activate ak
  note left of ak: yield 関数内<br>プロセス A の<br>ロック解放
  ak ->> au: usertrapret<br>プロセス A の<br>実行情報を復元
  deactivate ak
  activate au
  note left of au: プロセス A の<br>続きのプログラムを<br>そのまま実行する
  deactivate au
  ```
- システムコールで使うスリープロック
  ```mermaid
  sequenceDiagram
  Title: システムコールで使うスリープロック
  
  box プロセスA
      actor au as プロセスA(ユーザー)
      actor ak as プロセスA(カーネル)
  end
  actor sch as スケジューラ
  box プロセスB
      actor bk as プロセスB(カーネル)
      actor bu as プロセスB(ユーザー)
  end
  
  activate au
  au ->> ak: uservec 実行<br>プロセス A の<br>実行情報を保存
  deactivate au
  activate ak
  note left of au: システムコールで<br>ソフトウェア<br>割り込み
  note left of ak: システムコール内<br>システムコール用<br>スピンロック取得
  note left of ak: sleep 関数内<br>プロセス A<br>ロック取得
  note left of ak: sleep 関数内<br>システムコール用<br>スピンロック解放
  note left of ak: sleep 関数内<br>sched 関数実行
  ak ->> sch: sched 関数内<br>swtch
  deactivate ak
  
  activate sch
  note right of sch: プロセス A<br>ロック解放
  note left of sch: プロセス B の<br>ロック取得
  note left of sch: scheduler 関数内<br>プロセス B の<br>>swtch 実行
  sch ->> bk: swtch
  deactivate sch
  
  activate bk
  note right of bk: プロセス B の<br>ロック解放
  bk ->> bu: usertrapret<br>プロセス B の<br>実行情報を復元
  deactivate bk
  activate bu
  note right of bu: プロセス B の<br>続きのプログラムを<br>そのまま実行する
  deactivate bu
  
  activate sch
  note right of sch: プロセス A の<br>ロック取得
  note right of sch: scheduler 関数内<br>プロセス A の<br>swtch 実行
  sch ->> ak: swtch
  deactivate sch
  
  activate ak
  note left of ak: sleep 関数内<br>プロセス A の<br>ロック解放
  note left of ak: sleep 関数内<br>システムコール用<br>スピンロック取得
  note left of ak: システムコール内<br>続きの処理を実行
  ak ->> au: usertrapret<br>プロセス A の<br>実行情報を復元
  deactivate ak
  activate au
  note left of au: プロセス A の<br>続きのプログラムを<br>そのまま実行する
  deactivate au
  ```

### マルチプレクス
- 

## xv6 構造体

- proc

  ``` 
  struct proc {
    struct spinlock lock;
  
    // p->lock must be held when using these:
    enum procstate state;        // Process state
    void *chan;                  // If non-zero, sleeping on chan
    int killed;                  // If non-zero, have been killed
    int xstate;                  // Exit status to be returned to parent's wait
    int pid;                     // Process ID
  
    // wait_lock must be held when using this:
    struct proc *parent;         // Parent process
  
    // these are private to the process, so p->lock need not be held.
    uint64 kstack;               // Virtual address of kernel stack
    uint64 sz;                   // Size of process memory (bytes)
    pagetable_t pagetable;       // User page table
    struct trapframe *trapframe; // data page for trampoline.S
    struct context context;      // swtch() here to run process
    struct file *ofile[NOFILE];  // Open files
    struct inode *cwd;           // Current directory
    char name[16];               // Process name (debugging)
  };
  ```

- trapframe
  - : 現在のプロセスのカーネルスタックへのポインタ，現在の CPU の hartid, usertrap のアドレス，カーネルの
    ページテーブルのアドレス．uservec はそれらの情報を利用して satp をカーネル
    ページテーブルに切り替え，そして usertrap を呼び出します．

## RISC-V の仕様 (見返せると便利な項目を抜粋)

- アセンブリ
  - レジスタ関連
    ``` 
    メモリ操作
    レジスタraの値をsp+8番地のメモリにストア
    
      sd ra,8(sp)
    sp+8番地のメモリの値をレジスタraにロード
    
      ld ra,8(sp)
    ```
- レジスタ
  - 汎用レジスタ
      - 整数レジスタ
        | Register | ABI Name | Description                       | Saver  |
        | -------- | -------- | --------------------------------- | ------ |
        | x0       | zero     | Hard-wired zero                   |        |
        | x1       | ra       | Return address                    | Caller |
        | x2       | sp       | Stack pointer                     | Callee |
        | x3       | gp       | Global pointer                    |        |
        | x4       | tp       | Thread pointer                    |        |
        | x5       | t0       | Temporary/alternate link register | Caller |
        | x6       | t1       | Temporaries                       | Caller |
        | x7       | t2       | Temporaries                       | Caller |
        | x8       | s0/fp    | Saved register/frame pointer      | Callee |
        | x9       | s1       | Saved register                    | Callee |
        | x10      | a0       | Function arguments/return values  | Caller |
        | x11      | a1       | Function arguments/return values  | Caller |
        | x12      | a2       | Function arguments                | Caller |
        | x13      | a3       | Function arguments                | Caller |
        | x14      | a4       | Function arguments                | Caller |
        | x15      | a5       | Function arguments                | Caller |
        | x16      | a6       | Function arguments                | Caller |
        | x17      | a7       | Function arguments                | Caller |
        | x18      | s2       | Saved registers                   | Callee |
        | x19      | s3       | Saved registers                   | Callee |
        | x20      | s4       | Saved registers                   | Callee |
        | x21      | s5       | Saved registers                   | Callee |
        | x22      | s6       | Saved registers                   | Callee |
        | x23      | s7       | Saved registers                   | Callee |
        | x24      | s8       | Saved registers                   | Callee |
        | x25      | s9       | Saved registers                   | Callee |
        | x26      | s10      | Saved registers                   | Callee |
        | x27      | s11      | Saved registers                   | Callee |
        | x28      | t3       | Temporaries                       | Caller |
        | x29      | t4       | Temporaries                       | Caller |
        | x30      | t5       | Temporaries                       | Caller |
        | x31      | t6       | Temporaries                       | Caller |
      - 浮動小数点レジスタ
        | Register | ABI Name | Description                | Saver  |
        | -------- | -------- | -------------------------- | ------ |
        | f0       | ft0      | FP temporaries             | Caller |
        | f1       | ft1      | FP temporaries             | Caller |
        | f2       | ft2      | FP temporaries             | Caller |
        | f3       | ft3      | FP temporaries             | Caller |
        | f4       | ft4      | FP temporaries             | Caller |
        | f5       | ft5      | FP temporaries             | Caller |
        | f6       | ft6      | FP temporaries             | Caller |
        | f7       | ft7      | FP temporaries             | Caller |
        | f8       | fs0      | FP saved registers         | Callee |
        | f9       | fs1      | FP saved registers         | Callee |
        | f10      | fa0      | FP arguments/return values | Caller |
        | f11      | fa1      | FP arguments/return values | Caller |
        | f12      | fa2      | FP arguments               | Caller |
        | f13      | fa3      | FP arguments               | Caller |
        | f14      | fa4      | FP arguments               | Caller |
        | f15      | fa5      | FP arguments               | Caller |
        | f16      | fa6      | FP arguments               | Caller |
        | f17      | fa7      | FP arguments               | Caller |
        | f18      | fs2      | FP saved registers         | Callee |
        | f19      | fs3      | FP saved registers         | Callee |
        | f20      | fs4      | FP saved registers         | Callee |
        | f21      | fs5      | FP saved registers         | Callee |
        | f22      | fs6      | FP saved registers         | Callee |
        | f23      | fs7      | FP saved registers         | Callee |
        | f24      | fs8      | FP saved registers         | Callee |
        | f25      | fs9      | FP saved registers         | Callee |
        | f26      | fs10     | FP saved registers         | Callee |
        | f27      | fs11     | FP saved registers         | Callee |
        | f28      | ft8      | FP temporaries             | Caller |
        | f29      | ft9      | FP temporaries             | Caller |
        | f30      | ft10     | FP temporaries             | Caller |
        | f31      | ft11     | FP temporaries             | Caller |

      - プログラムカウンタなどは別にあるのだろうか？
      
  - 制御レジスタ (CSR: Control and Status Register)

      - mstatus レジスタ

      - 高速な割り込み動作を実現するための CSR (mideleg, medeleg)

      - satp レジスタ: ページングテーブルのアドレスを入れる

      - 割り込みや例外を扱うための CSR

          | レジスタ名      | レジスタ説明                   | 概要                                                         |
          | :-------------- | :----------------------------- | ------------------------------------------------------------ |
          | mtvec / stvec   | トラップベースアドレスレジスタ | 割り込み・例外が発生した場合にジャンプするPCを格納しておきます。 |
          | mepc / sepc     | 例外プログラムカウンタレジスタ | 例外が発生した命令が格納されているプログラムカウンタを格納しています。 |
          | mcause / scause | 例外要因レジスタ               | 割り込み・例外が発生した要因を格納しています。               |
          | mtval / stval   | マシンソフトウェア割り込み     | 例外の情報を格納します。このレジスタに書き込まれる値は、発生する例外の種類に応じて異なります。 |

- 割り込みコード

  - | コード番号 | 愛用                             |
    | :--------- | :------------------------------- |
    | 0          | ユーザソフトウェア割り込み       |
    | 1          | スーパバイザソフトウェア割り込み |
    | 2          | 予約                             |
    | 3          | マシンソフトウェア割り込み       |
    | 4          | ユーザタイマ割り込み             |
    | 5          | スーパバイザタイマ割り込み       |
    | 6          | 予約                             |
    | 7          | マシンタイマ割り込み             |
    | 8          | ユーザ外部割込み                 |
    | 9          | スーパバイザ外部割込み           |
    | 10         | 予約                             |
    | 11         | マシン外部割込み                 |
    | >=12       | 予約                             |

- 例外コード

  - | コード番号 | 概要                                                         |
    | :--------- | :----------------------------------------------------------- |
    | 0          | 命令アドレスミスアライン例外                                 |
    | 1          | 命令アクセス例外                                             |
    | 2          | 不定命令例外                                                 |
    | 3          | ブレークポイント例外                                         |
    | 4          | ロードアドレスミスアライン例外                               |
    | 5          | ロードアクセス例外                                           |
    | 6          | ストア/アトミックアクセスミスアライン例外                    |
    | 7          | ストア/アトミックアクセス例外                                |
    | 8          | **ユーザモードからのEnvironment Call** (ユーザモードからのシステムコール) |
    | 9          | スーパバイザモードからのEnvironment Call                     |
    | 10         | 予約                                                         |
    | 11         | マシンモードからのEnvironmental Call                         |
    | 12         | ページアクセス例外（命令フェッチ）                           |
    | 13         | ページアクセス例外（ロード）                                 |
    | 14         | 予約                                                         |
    | 15         | ページアクセス例外（ストア・アトミック）                     |
    | >= 16      | 予約                                                         |

